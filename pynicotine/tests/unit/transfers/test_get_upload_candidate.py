# SPDX-FileCopyrightText: 2022-2025 Nicotine+ Contributors
# SPDX-License-Identifier: GPL-3.0-or-later

import os
import shutil

from unittest import TestCase

from pynicotine.config import config
from pynicotine.core import core
from pynicotine.transfers import Transfer
from pynicotine.slskmessages import increment_token
from pynicotine.slskmessages import initial_token

DATA_FOLDER_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), "temp_data")
NUM_ALLOWED_NONE = 2


class GetUploadCandidateTest(TestCase):

    # pylint: disable=protected-access

    def setUp(self):

        self.token = initial_token()

        config.set_data_folder(DATA_FOLDER_PATH)
        config.set_config_file(os.path.join(DATA_FOLDER_PATH, "temp_config"))

        core.init_components(enabled_components={
            "users", "pluginhandler", "shares", "statistics", "uploads", "buddies"}
        )
        core.start()

        core.users.privileged = {"puser1", "puser2"}
        core.uploads.transfers.clear()

    def tearDown(self):
        core.quit()

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(DATA_FOLDER_PATH)

    def add_transfers(self, users, is_active=False):

        transfer_list = []

        for username in users:
            virtual_path = f"{username}/{len(core.uploads.transfers)}"
            transfer = Transfer(username, virtual_path)

            if is_active:
                core.uploads._activate_transfer(transfer, self.token)
                self.token = increment_token(self.token)
            else:
                core.uploads._enqueue_transfer(transfer)

            transfer_list.append(transfer)
            core.uploads._append_transfer(transfer)
            core.uploads._update_transfer(transfer)

        return transfer_list

    def set_finished(self, transfer):
        core.uploads._finish_transfer(transfer)
        core.uploads._clear_transfer(transfer)

    def consume_transfers(self, queued, in_progress, clear_first=False):
        """Call core.uploads.get_upload_candidate until no uploads are left.

        Transfers should be added to core.uploads in the desired starting
        states already.

        One in progress upload will be removed each time get_upload_candidate
        is called.

        `queued` and `in_progress` should contain the transfers in those states.

        `clear_first` indicates whether the upload candidate should be
        generated after the in progress upload is marked finished or before.

        All candidates received are returned in a list.
        """

        candidates = []
        none_count = 0  # prevent infinite loop in case of bug or bad test setup

        while len(core.uploads.transfers) > 0 and none_count < NUM_ALLOWED_NONE:

            # "finish" one in progress transfer, if any
            if clear_first and in_progress:
                self.set_finished(in_progress.pop(0))

            candidate, _has_active_uploads = core.uploads._get_upload_candidate()

            if not clear_first and in_progress:
                self.set_finished(in_progress.pop(0))

            if not candidate:
                none_count += 1
                candidates.append(None)
                continue

            none_count = 0

            queued.remove(candidate)
            core.uploads._dequeue_transfer(candidate)

            candidates.append(candidate)
            in_progress.append(candidate)
            core.uploads._activate_transfer(candidate, self.token)

            self.token = increment_token(self.token)

        return candidates

    def base_test(self, queued, in_progress, expected, round_robin=False, clear_first=False):

        config.sections["transfers"]["fifoqueue"] = not round_robin

        queued_transfers = self.add_transfers(queued)
        in_progress_transfers = self.add_transfers(in_progress, is_active=True)

        candidates = self.consume_transfers(queued_transfers, in_progress_transfers, clear_first=clear_first)
        users = [transfer.username if transfer else None for transfer in candidates]

        # `expected` should contain `None` in cases where there aren't
        # expected to be any queued users without existing in progress uploads
        self.assertEqual(users, expected)

    def test_round_robin_basic(self):

        self.base_test(
            queued=[
                "user1",
                "user1",
                "user2",
                "user2",
                "user3",
                "user3"
            ],
            in_progress=[],
            expected=[
                "user1",
                "user2",
                "user3",
                "user1",
                "user2",
                "user3",
                None
            ],
            round_robin=True
        )

    def test_round_robin_no_contention(self):

        self.base_test(
            queued=[
                "user1",
                "user1",
                "user2",
                "user2",
                "user3",
                "user3"
            ],
            in_progress=[],
            expected=[
                "user1",
                "user2",
                "user3",
                "user1",
                "user2",
                "user3",
                None
            ],
            round_robin=True,
            clear_first=True
        )

    def test_round_robin_one_user(self):

        self.base_test(
            queued=[
                "user1",
                "user1"
            ],
            in_progress=[],
            expected=[
                "user1",
                None,
                "user1",
                None
            ],
            round_robin=True
        )

    def test_round_robin_returning_user(self):

        self.base_test(
            queued=[
                "user1",
                "user1",
                "user2",
                "user2",
                "user2",
                "user3",
                "user3",
                "user3",
                "user1",
                "user1"
            ],
            in_progress=[],
            expected=[
                "user1",
                "user2",
                "user3",
                "user1",
                "user2",
                "user3",
                "user1",
                "user2",
                "user3",
                "user1",
                None
            ],
            round_robin=True
        )

    def test_round_robin_in_progress(self):

        self.base_test(
            queued=[
                "user1",
                "user1",
                "user2",
                "user2"
            ],
            in_progress=[
                "user1"
            ],
            expected=[
                "user2",
                "user1",
                "user2",
                "user1",
                None
            ],
            round_robin=True
        )

    def test_round_robin_privileged(self):

        self.base_test(
            queued=[
                "user1",
                "user2",
                "puser1",
                "puser1",
                "puser2"
            ],
            in_progress=[],
            expected=[
                "puser1",
                "puser2",
                "puser1",
                "user1",
                "user2",
                None
            ],
            round_robin=True
        )

    def test_fifo_basic(self):

        self.base_test(
            queued=[
                "user1",
                "user1",
                "user2",
                "user2",
                "user3",
                "user3"
            ],
            in_progress=[],
            expected=[
                "user1",
                "user2",
                "user1",
                "user2",
                "user3",
                None,
                "user3",
                None
            ]
        )

    def test_fifo_robin_no_contention(self):

        self.base_test(
            queued=[
                "user1",
                "user1",
                "user2",
                "user2",
                "user3",
                "user3"
            ],
            in_progress=[],
            expected=[
                "user1",
                "user1",
                "user2",
                "user2",
                "user3",
                "user3",
                None
            ],
            clear_first=True
        )

    def test_fifo_one_user(self):

        self.base_test(
            queued=[
                "user1",
                "user1"
            ],
            in_progress=[],
            expected=[
                "user1",
                None,
                "user1",
                None
            ]
        )

    def test_fifo_returning_user(self):

        self.base_test(
            queued=[
                "user1",
                "user1",
                "user2",
                "user2",
                "user2",
                "user3",
                "user3",
                "user3",
                "user1",
                "user1"
            ],
            in_progress=[],
            expected=[
                "user1",
                "user2",
                "user1",
                "user2",
                "user3",
                "user2",
                "user3",
                "user1",
                "user3",
                "user1",
                None
            ]
        )

    def test_fifo_in_progress(self):

        self.base_test(
            queued=[
                "user1",
                "user1",
                "user2",
                "user2"
            ],
            in_progress=[
                "user1"
            ],
            expected=[
                "user2",
                "user1",
                "user2",
                "user1",
                None
            ]
        )

    def test_fifo_privileged(self):

        self.base_test(
            queued=[
                "user1",
                "user2",
                "puser1",
                "puser1",
                "puser2"
            ],
            in_progress=[],
            expected=[
                "puser1",
                "puser2",
                "puser1",
                "user1",
                "user2",
                None
            ]
        )
