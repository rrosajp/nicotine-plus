<!--
  SPDX-FileCopyrightText: 2004-2025 Nicotine+ Contributors
  SPDX-FileCopyrightText: 2003-2004 Nicotine Contributors
  SPDX-FileCopyrightText: 2002-2003 PySoulSeek Contributors
  SPDX-License-Identifier: GPL-3.0-or-later
-->

# Release Notes

The current stable version of Nicotine+ is available at [DOWNLOADS.md](doc/DOWNLOADS.md).

You can run the latest unstable build of Nicotine+ to test recent changes and bug fixes, see [TESTING.md](doc/TESTING.md).


## Version 3.3.10 (March 10, 2025)

### Corrections

 * Fixed file transfers not starting

### Issues closed on GitHub

 * Downloads stuck on Queued ([#3320](https://github.com/nicotine-plus/nicotine-plus/issues/3320))


## Version 3.3.9 (March 9, 2025)

### Corrections

 * Fixed a crash when rescanning shared files in some cases
 * Fixed column widths not being remembered for certain columns
 * Improved readability of long file paths in File Properties dialog
 * Fixed minor inconsistencies in the GUI

### Issues closed on GitHub

 * Diacritics starting names are in wrong order (at the end of the list) - languages drop-down menu ([#3295](https://github.com/nicotine-plus/nicotine-plus/issues/3295))
 * Setting the width of the columns is not remembered ([#3296](https://github.com/nicotine-plus/nicotine-plus/issues/3296))
 * Can't boot after deleting app and reinstalling it ([#3308](https://github.com/nicotine-plus/nicotine-plus/issues/3308))


## Version 3.3.8 (February 24, 2025)

### Changes

 * Added isolated mode (`nicotine --isolated`) for standalone environments (e.g. Docker containers)
 * Added Czech translation (thank you @slrslr)
 * Added Tamil translation (thank you @TamilNeram)
 * Optimized reading of large chat logs
 * Optimized upload queue position requests
 * Show number of scanned folders while rescanning shares
 * Skip unit tests requiring network connection by default

### Corrections

 * Fixed a crash when closing font chooser dialogs in older GTK 4 versions
 * Fixed broken tray icons in the Flatpak package
 * Fixed incorrect download folder names in rare cases
 * Fixed RTL text direction being used with LTR languages
 * Fixed libadwaita being enabled by accident in Budgie desktop environment
 * Windows: Fixed a crash on systems with outdated Vulkan drivers
 * Windows: Fixed a crash on systems with Proxifier enabled
 * Windows: Fixed main window minimizing when closing dialogs
 * Windows: Fixed broken window size when restoring from tray
 * macOS: Fixed a crash on startup with Apple Silicon build

### Issues closed on GitHub

 * Slowness when uploading large amount of files ([#3199](https://github.com/nicotine-plus/nicotine-plus/issues/3199))
 * App told me to report this. ([#3218](https://github.com/nicotine-plus/nicotine-plus/issues/3218))
 * Nicotine 3.3.7 issue with Sonoma 14.7.2 : impossible to start app ! ([#3227](https://github.com/nicotine-plus/nicotine-plus/issues/3227))
 * Closing the lil Wishlist window minimizes the entire app ([#3230](https://github.com/nicotine-plus/nicotine-plus/issues/3230))
 * Remember and restore window size and position when opening an application from the tray ([#3236](https://github.com/nicotine-plus/nicotine-plus/issues/3236))
 * Progress indication when (re-)scanning shares ([#3246](https://github.com/nicotine-plus/nicotine-plus/issues/3246))
 * Czech language translation status ([#3248](https://github.com/nicotine-plus/nicotine-plus/issues/3248))
 * removed_parent_folders should only remove first occurence ([#3255](https://github.com/nicotine-plus/nicotine-plus/issues/3255))
 * Crash after update to newer version and found that older versions also crash now ([#3265](https://github.com/nicotine-plus/nicotine-plus/issues/3265))
 * The only valid location for the SVG icon on Linux is /usr/share/icons/hicolor/scalable/apps ([#3273](https://github.com/nicotine-plus/nicotine-plus/issues/3273))
 * UI layout with text direction Right-to-Left ([#3285](https://github.com/nicotine-plus/nicotine-plus/issues/3285))


## Version 3.3.7 (December 15, 2024)

### Changes

 * Grey out ignored usernames in room user lists
 * Automatically reconnect to the server when changing listening port
 * Always show number of upload slots on user profiles
 * Windows: Update Python from 3.11 to 3.12
 * macOS: Drop support for macOS Monterey due to reaching EOL

### Corrections

 * Fixed a crash when using file choosers in plugin settings
 * Fixed a crash when upgrading from Nicotine+ 1.4.1 and earlier
 * Fixed broken upload stats caused by Soulseek NS clients resuming >2 GB downloads
 * Fixed an issue where picking an emoji would clear existing text
 * Improved file transfer speeds in some cases
 * Windows: Reverted switch to Clang environment due to rare crashes

### Issues closed on GitHub

 * Banned and ignored users indicators ([#2100](https://github.com/nicotine-plus/nicotine-plus/issues/2100))
 * Allow N+ to update Port without restarting ([#2704](https://github.com/nicotine-plus/nicotine-plus/issues/2704))
 * Incorrect processing of passwords with special characters ([#3156](https://github.com/nicotine-plus/nicotine-plus/issues/3156))
 * 3.3.5 has same bug latest Test clients have about upload showing wrong upload ([#3162](https://github.com/nicotine-plus/nicotine-plus/issues/3162))
 * Cannot update nicotine+ ([#3167](https://github.com/nicotine-plus/nicotine-plus/issues/3167))
 * 3.3.6 crashes on launch on macOS due to broken rendering ([#3172](https://github.com/nicotine-plus/nicotine-plus/issues/3172))
 * GTK4-based app crashes with: TypeError: No means to translate argument or return value for 'GdkButtonEvent' ([#3176](https://github.com/nicotine-plus/nicotine-plus/issues/3176))
 * I get this error when i try to run Nicotine+ ([#3175](https://github.com/nicotine-plus/nicotine-plus/issues/3175))
 * A lot of dump files (gdbus) ([#3181](https://github.com/nicotine-plus/nicotine-plus/issues/3181))
 * Filechooser.py Window' object has no attribute 'widget' ([#3182](https://github.com/nicotine-plus/nicotine-plus/issues/3182))
 * \[3.3.7.dev1\] Windows Nightly builds libgcc_s_seh-1.dll is missing ([#3183](https://github.com/nicotine-plus/nicotine-plus/issues/3183))
 * \[Bug\]: Transfer Statistics Total Uploaded Size jumps to 32 EiB ([#3185](https://github.com/nicotine-plus/nicotine-plus/issues/3185))
 * Picking an emoji clears text in chat entry, rather than being appended to it ([#3197](https://github.com/nicotine-plus/nicotine-plus/issues/3197))
 * User logs off but items in queue slowly tick away from saying queued to logged off ([#3209](https://github.com/nicotine-plus/nicotine-plus/issues/3209))
 * Nicotine+ not working on Windows 10 since v3.3.6 ([#3210](https://github.com/nicotine-plus/nicotine-plus/issues/3210))


## Version 3.3.6 (October 15, 2024)

### Changes

 * Hide picture view when no user profile picture is present
 * GTK 4: Stop using old GL renderer
 * Windows: Reduced package size by switching to MSYS2's Clang environment

### Corrections

 * Important: Don't delete other unrelated files from incomplete download folder
 * Fixed a crash when editing and removing list rows in some cases
 * Fixed a regression where arrow keys no longer selected items in comboboxes
 * Minor fixes related to the tray icon implementation
 * GTK 3: Fixed an issue where the chat text entry could disappear
 * macOS: Fixed an issue where opening files and links no longer worked
 * macOS: Fixed a few keyboard shortcuts that no longer worked

### Issues closed on GitHub

 * 'Open in File Manager' does not work on 3.3.5 in macOS Monterey ([#3143](https://github.com/nicotine-plus/nicotine-plus/issues/3143))
 * Issues with selecting text on 3.3.5 in macOS Monterey ([#3144](https://github.com/nicotine-plus/nicotine-plus/issues/3144))
 * Horizontal adjustment of user profile ([#2865](https://github.com/nicotine-plus/nicotine-plus/issues/2865))
 * Files deleted on quit ([#3152](https://github.com/nicotine-plus/nicotine-plus/issues/3152))
 * the window does not close automatically and gets in the way ([#3157](https://github.com/nicotine-plus/nicotine-plus/issues/3157))


## Version 3.3.5 (September 22, 2024)

### Changes

 * Added `/plugin reload` subcommand for reloading a plugin
 * Added arrow key shortcuts to collapse/expand tree rows
 * Added a toggle for private room invitations to 'Chats' preferences
 * List all room members not currently joined in a private room
 * Incomplete files are now deleted when removing the download from the UI
 * Improvements to transfer speed accuracy in the UI
 * Grey out transfer rows with 'User logged off' status
 * Quitting from the tray menu asks for confirmation while uploads are active
 * Handle invalid password in Setup Assistant instead of opening the Preferences dialog
 * Large performance improvement when listing search results or adding transfers
 * Reduced memory and storage space used by the IP2Location database
 * macOS and Windows: Require GTK 4 unless `NICOTINE_GTK_VERSION=3` env variable is set

### Corrections

 * Fixed a rare crash related to peer connections
 * Fixed a rare crash when selecting a folder in the file chooser dialog
 * Fixed a possible memory error when reading data from a peer connection
 * Fixed issues related to downloads getting stuck when failing
 * Fixed issues related to transfer rows expanding when not supposed to
 * Fixed an issue where banning a user's IP did not remove their uploads
 * Fixed an issue where uploads would not start immediately in some cases
 * Fixed an issue where popovers could not be closed in some cases
 * Fixed an issue where some wishlist searches stopped working after closing their tabs
 * Fixed an issue where an auto-forwarded listening port would close when saving preferences
 * Fixed an issue where toggling search history did not update the history dropdown
 * Various accessibility fixes related to scrolling, text views and entry widgets
 * Various smaller fixes related to the Soulseek protocol implementation
 * Windows: Fixed an issue where the tray icon was visible despite being disabled
 * Windows: Fixed an issue where window prevented auto-hidden taskbar from showing
 * Windows: Fixed invalid list sort order with certain system locales
 * macOS: Fixed a crash when using Spanish system locale
 * macOS: Fixed an issue where window could not be restored after running in background
 * macOS: Fixed Ctrl-clicking not opening the context menu
 * macOS: Added a few missing keyboard shortcuts
 * GTK 3: Fixed a crash when pressing "Run in Background" in the confirmation dialog

### Issues closed on GitHub

 * Nicotine+ can't be launched from network drive on Windows ([#1843](https://github.com/nicotine-plus/nicotine-plus/issues/1843))
 * Really varied upload speeds ([#2219](https://github.com/nicotine-plus/nicotine-plus/issues/2219))
 * Right click with control click doesn't work on mac with trackpad ([#2724](https://github.com/nicotine-plus/nicotine-plus/issues/2724))
 * Bad user experience with Windows-like buttons on Nicotine 3.3.0 ([#2880](https://github.com/nicotine-plus/nicotine-plus/issues/2880))
 * Downloads stuck on 'Queued' ([#2926](https://github.com/nicotine-plus/nicotine-plus/issues/2926))
 * User rows expanding when collapse all enabled ([#2969](https://github.com/nicotine-plus/nicotine-plus/issues/2969))
 * Connection closed and other connectivity problems ([#2978](https://github.com/nicotine-plus/nicotine-plus/issues/2978))
 * Crash on Mac OS Monterey 12.7.5 (Intel) - Nicotine+ Version: 3.3.5.dev1 ([#3016](https://github.com/nicotine-plus/nicotine-plus/issues/3016))
 * "Ok" on Network Closes Port ([#3020](https://github.com/nicotine-plus/nicotine-plus/issues/3020))
 * Python Memory Error ([#3022](https://github.com/nicotine-plus/nicotine-plus/issues/3022))
 * nowplaying - other should decode bytes ([#3039](https://github.com/nicotine-plus/nicotine-plus/issues/3039))
 * Newly started downloads will open a collapsed thread? ([#3044](https://github.com/nicotine-plus/nicotine-plus/issues/3044))
 * Crash on MBP Ventura 13.6.7 ([#3045](https://github.com/nicotine-plus/nicotine-plus/issues/3045))
 * Sorting order of files is broken because of characters not in current codepage ([#3052](https://github.com/nicotine-plus/nicotine-plus/issues/3052))
 * Adding SMB share on linux results in critical error ([#3056](https://github.com/nicotine-plus/nicotine-plus/issues/3056))
 * Crash, build 8 July ([#3057](https://github.com/nicotine-plus/nicotine-plus/issues/3057))
 * Arrow key shortcuts to expand/collapse groups ([#3060](https://github.com/nicotine-plus/nicotine-plus/issues/3060))
 * Nicotine+ crashing when trying to browse public shares (on MacOS 15 Public Beta) ([#3063](https://github.com/nicotine-plus/nicotine-plus/issues/3063))
 * Bug at the last update Version: 3.3.5.dev2 ([#3067](https://github.com/nicotine-plus/nicotine-plus/issues/3067))
 * "end" key works incorrectly at the "uploads" tab. ([#3068](https://github.com/nicotine-plus/nicotine-plus/issues/3068))
 * Upload I/O error: cannot fit 'int' into an offset-sized integer ([#3077](https://github.com/nicotine-plus/nicotine-plus/issues/3077))
 * critic error on 3.3.4 ([#3080](https://github.com/nicotine-plus/nicotine-plus/issues/3080))
 * Client closes after PC waking from sleep ([#3082](https://github.com/nicotine-plus/nicotine-plus/issues/3082))
 * Files are not shared ([#3083](https://github.com/nicotine-plus/nicotine-plus/issues/3083))
 * Sudden Crash when loading text in the search bar ([#3087](https://github.com/nicotine-plus/nicotine-plus/issues/3087))
 * Input history scroll ([#3106](https://github.com/nicotine-plus/nicotine-plus/issues/3106))
 * Files get downloaded twice ([#3107](https://github.com/nicotine-plus/nicotine-plus/issues/3107))
 * App window not showing up with Wayland/NVidia ([#3108](https://github.com/nicotine-plus/nicotine-plus/issues/3108))
 * Nicotine+ crashes on Mac when browsing for buddy shares via Shares menu ([#3110](https://github.com/nicotine-plus/nicotine-plus/issues/3110))
 * Leave "Wishlist" windows open/active after initiating a search & Easier method to initiate search ([#3114](https://github.com/nicotine-plus/nicotine-plus/issues/3114))
 * crash after download try ([#3119](https://github.com/nicotine-plus/nicotine-plus/issues/3119))
 * Wishlist result notification is emitted even when disabled ([#3123](https://github.com/nicotine-plus/nicotine-plus/issues/3123))
 * Crash while running on background ([#3130](https://github.com/nicotine-plus/nicotine-plus/issues/3130))
 * Cannot browse another user's files in MacOS 15.0 (24A335) ([#3134](https://github.com/nicotine-plus/nicotine-plus/issues/3134))
 * Wrong hotkeys on mac. Should be Cmd instead of Ctrl ([#3139](https://github.com/nicotine-plus/nicotine-plus/issues/3139))


## Version 3.3.4 (May 6, 2024)

### Corrections

 * Fixed "Format codes" link not opening in the preferred browser
 * Windows: Fixed regression in scrolling performance

### Issues closed on GitHub

 * Scrolling performance suddenly abysmal (again) ([#3000](https://github.com/nicotine-plus/nicotine-plus/issues/3000))
 * Can't access "Format Codes" link in settings through left mouse click on 3.3.3 ([#3001](https://github.com/nicotine-plus/nicotine-plus/issues/3001))
 * Sometimes, Nicotine+ (3.3.3) window doesn't open on top when other windows already opened full screen on the desktop. ([#3002](https://github.com/nicotine-plus/nicotine-plus/issues/3002))


## Version 3.3.3 (May 5, 2024)

### Changes

 * Performance improvements when searching for common files
 * Improved search result matching for non-Latin languages
 * Minor accessibility improvements
 * Updated translations
 * GTK 3: Restored X11 tray icon implementation for compatibility with older systems

### Corrections

 * Fixed a rare crash when changing grouping mode in transfer tabs
 * Fixed a rare crash when closing Browse Shares tab
 * Fixed a rare crash when initializing an upload
 * Fixed a rare crash when double-clicking a download
 * Fixed an issue where passwords were not remembered after changing them
 * Fixed an issue where number of shared files was only updated on startup (regression in 3.3.2)
 * Fixed an issue where transfers displayed incorrect "User logged off" status in some cases
 * Fixed an issue where chat history entry completion no longer worked
 * Fixed an issue where UPnP did not work on MikroTik routers
 * Fixed missing button labels in certain dialogs
 * Fixed some small memory leaks
 * Avoid selecting new transfers while tab is active
 * Remember selected folder when refreshing local shares
 * Windows: Fixed Alt+1-9 tab shortcuts interfering with Alt codes
 * Windows: Fixed window not minimizing when clicking task bar icon
 * Windows: Fixed title bar buttons requiring two clicks to activate
 * Snap: Fixed an issue where the file chooser displayed the wrong initial folder
 * Snap: Fixed an issue where folders shared from external drives were unavailable after remounting
 * Termux: Fixed an issue where connecting to the server failed

### Issues closed on GitHub

 * Bad user experience with Windows-like buttons on Nicotine 3.3.0 ([#2880](https://github.com/nicotine-plus/nicotine-plus/issues/2880))
 * Auto-selection of new transfers ([#2901](https://github.com/nicotine-plus/nicotine-plus/issues/2901))
 * Nicotine+ 3.3.2 displays user as logged off while the transfers are active ([#2909](https://github.com/nicotine-plus/nicotine-plus/issues/2909))
 * No icon in taskbar when running in background ([#2928](https://github.com/nicotine-plus/nicotine-plus/issues/2928))
 * Set 'Finished' status instead of 'Filtered' for finished transfers in case the directory had files matching download filtering pattern ([#2932](https://github.com/nicotine-plus/nicotine-plus/issues/2932))
 * Refresh Files button not working ([#2937](https://github.com/nicotine-plus/nicotine-plus/issues/2937))
 * Nictotine Hard fail trying to get pointer ([#2943](https://github.com/nicotine-plus/nicotine-plus/issues/2943))
 * 3.3.2 - System Tray Icons Don't Appear ([#2944](https://github.com/nicotine-plus/nicotine-plus/issues/2944))
 * Sudden crash ([#2950](https://github.com/nicotine-plus/nicotine-plus/issues/2950))
 * bug on checking transfers ([#2953](https://github.com/nicotine-plus/nicotine-plus/issues/2953))
 * UPnP: Failed to forward external port 2234: HTTP Error 500: Internal Server Error ([#2955](https://github.com/nicotine-plus/nicotine-plus/issues/2955))
 * 0 Shares on Profile ([#2956](https://github.com/nicotine-plus/nicotine-plus/issues/2956))
 * Crash when double clicking download row ([#2961](https://github.com/nicotine-plus/nicotine-plus/issues/2961))
 * Nicotine+ 3.3.2 permission denied to port 2234 on Fedora 39 ([#2968](https://github.com/nicotine-plus/nicotine-plus/issues/2968))
 * This option is doesn't work on Nicotine+ 3.3.3 rc2 ([#2969](https://github.com/nicotine-plus/nicotine-plus/issues/2969))
 * Num lock state is inverted ([#2977](https://github.com/nicotine-plus/nicotine-plus/issues/2977))
 * Random crash ([#2982](https://github.com/nicotine-plus/nicotine-plus/issues/2982))
 * Found another bug ([#2988](https://github.com/nicotine-plus/nicotine-plus/issues/2988))
 * Arbitrary Critical Error ([#2996](https://github.com/nicotine-plus/nicotine-plus/issues/2996))


## Version 3.3.2 (February 25, 2024)

### Corrections

 * Fixed a crash when adding transfers while in ungrouped mode
 * Fixed an issue where dialog message labels were not read by screen readers
 * Snap: Fixed screen reader detection for enabling GTK 3


## Version 3.3.1 (February 24, 2024)

### Changes

 * Added function to manually search a wishlist item
 * Exclude the Synology "#snapshot" and "#recycle" folders from Shares (thank you @toineenzo)
 * Improved performance when loading transfers on startup
 * Implemented server code 160 (Excluded Search Phrases)
 * macOS: update visual style of window controls to resemble native apps

### Corrections

 * Important: Fixed critical error crash at startup on rejected login (regression in 3.3.0)
 * Avoid a rare crash (log a FIXME error) when clearing a transfer not present in list
 * Fixed a crash when using up/down arrow keys in empty combo box widget
 * Fixed an issue that prevented the Now Playing Sender plugin from working
 * Fixed an issue that prevented the /away command from working
 * Fixed an issue connecting to certain distributed peers
 * Fixed broken scrolling in font chooser on GTK 4
 * Fixed an issue where private chat messages did not load in rare cases
 * Fixed an issue where retrying an upload did not start it immediately
 * Fixed an issue where the chat room tab order was incorrect after restarting
 * Removed a keyboard focus trap during tab navigation
 * Linux: Fixed an issue where binding to a virtual private network interface did not work
 * Windows: Fixed an issue with flickering/invisible window when maximized with auto-hide taskbar
 * Windows: Fixed an issue where the file manager/audio player window was hidden
 * Windows: Fixed an issue downloading files containing control characters in the path
 * Windows: Fixed an issue where reverse file paths did not work for older downloads
 * macOS: Fixed an issue where Nicotine+ did not launch on Monterey systems (thank you @thep50)
 * macOS: Fixed an issue where window was not maximized on startup
 * macOS: Added missing keyboard shortcuts for text entries/views

### Issues closed on GitHub

 * Nicotine+ crashes on startup - BufferError ([#2850](https://github.com/nicotine-plus/nicotine-plus/issues/2850))
 * Failure to launch 3.3.0 on Mac ([#2852](https://github.com/nicotine-plus/nicotine-plus/issues/2852))
 * Implement server code 160 ([#2854](https://github.com/nicotine-plus/nicotine-plus/issues/2854))
 * Unable to resize window in Mac Silicon app ([#2857](https://github.com/nicotine-plus/nicotine-plus/issues/2857))
 * Nicotine 3.3.0 Flickering when changing tabs ([#2859](https://github.com/nicotine-plus/nicotine-plus/issues/2859))
 * "Open in File Manager" not working on Windows ([#2860](https://github.com/nicotine-plus/nicotine-plus/issues/2860))
 * 3.3.0: does not connect to server via tun0 (vpn) ([#2861](https://github.com/nicotine-plus/nicotine-plus/issues/2861))
 * Issue selecting text on macOS Monterey ([#2862](https://github.com/nicotine-plus/nicotine-plus/issues/2862))
 * Retry on uploads no longer works ([#2864](https://github.com/nicotine-plus/nicotine-plus/issues/2864))
 * Interest recommendations ([#2866](https://github.com/nicotine-plus/nicotine-plus/issues/2866))
 * Crash after clearing download folder with 1 file in it ([#2869](https://github.com/nicotine-plus/nicotine-plus/issues/2869))
 * Bug Crash ([#2872](https://github.com/nicotine-plus/nicotine-plus/issues/2872))
 * Cannot save file error ([#2888](https://github.com/nicotine-plus/nicotine-plus/issues/2888))


## Version 3.3.0 (February 1, 2024)

### Changes

 * Enabled GTK 4 support by default for new visual style on Windows, macOS and GNOME
 * Added "Chat History" popover to view all previous private chats with users
 * Added generic file type search result filters (audio \| image \| video \| text \| archive \| executable)
 * Added audio duration search result filter (HH:MM:SS \| MM:SS \| Seconds)
 * Added support for phrase searching using quotation marks
 * Added path bar when browsing user shares
 * Added option to make specific shares available to trusted buddies only
 * Added option to wait for active uploads to finish before quitting Nicotine+
 * Added function to send a private message to all online buddies and users in upload queue
 * Added a warning dialog if shared folders are unavailable before rescanning
 * Added dropdown menu listing all open tabs
 * Added function to reopen closed tab with Ctrl+Shift+T shortcut
 * Added option to show exact file sizes in bytes
 * Added popovers in the status bar for selecting download and upload speed limits
 * Added option to configure text view font
 * Added function to clear all deleted downloads that no longer exist on disk
 * Added function to re-enter search when right-clicking search tabs
 * Added preference to choose user interface language
 * Added wishlist results found notification
 * Added option to set custom handlers for opening downloaded files
 * Added file type icons to file lists
 * Added button to view personal profile
 * Added buttons in Preferences to open download folder locations in file manager
 * Added total size of all selected files to window title in the "File Properties" dialog
 * Added new command system for plugins (type /help for a list of available commands)
 * Added keyboard input with readline command editing and history to headless CLI
 * Added support for NAT-PMP port forwarding
 * Windows: Added option to bind Nicotine+ to a specific network interface
 * macOS: Added native support for Apple Silicon
 * Changed "Bitrate" column to "Quality" for displaying sample rate of uncompressed files
 * Allow search result filters to be restored after clicking the "Clear Filters" button
 * Restore initial list order when pressing the column header of a sorted column
 * Remember last sorted column after restarting
 * Filter out irrelevant folders when searching a user's shares
 * Allow selecting multiple folders in a user's shares
 * Insert new private chat tabs before older ones
 * Resuming a single filtered download allows for bypassing download filter
 * Transfer log files are now split into per-session download and upload logs
 * Retry downloads limited due to maximum queue/file sizes more frequently
 * Performance improvements when scanning and accessing shares
 * Banned users can no longer read self descriptions on user profiles
 * Moved buddy list position option from view menu to Preferences dialog
 * Removed View menu, since all options in this menu can be toggled by other means
 * Removed "Auto-join" check box, joined chat rooms are now remembered between sessions
 * Removed command alias system in favor of plugin commands
 * Removed some redundant user interface options and unified some configuration preferences
 * Removed python3-gdbm dependency
 * Bumped minimum Python version requirement to 3.6
 * Bumped minimum GTK 3 version requirement to 3.22.30
 * Windows: Removed support for Windows 7, 8 and 8.1, as well as 32-bit systems
 * macOS: Removed support for macOS 10.15 and 11
 * Completed Soulseek protocol implementation of distributed peers, bumped protocol version to 160.2

### Corrections

 * Fixed a crash when downloading filenames containing special characters on some systems
 * Fixed a crash when clicking a slsk:// root folder URL without a trailing slash
 * Fixed an issue where enabling/disabling chat completions did not update them properly in some cases
 * Fixed an issue where the global room feed was not restored on startup
 * Fixed an issue where important tabs (e.g. chat highlights) were not always marked as such
 * Fixed an issue where search results were not sent in rare cases
 * Fixed an issue where sharing a lot of files could result in messages about not sharing
 * Fixed an issue where finished downloads were not always automatically cleared
 * Fixed an issue where recursively downloading a folder would include unwanted folders in some cases
 * Fixed an issue where recommendations with a negative rating did not appear
 * Improved performance when many queued transfers are added or retried
 * Implemented monotonic timers to ensure that transfers are unaffected by system clock adjustments
 * Check file modified times instead of folder when rescanning to ensure shares are properly updated
 * Stop loading a user's shares after closing the tab, to avoid wasting bandwidth
 * Leech Detector plugin no longer sends message to sharing users with incorrect file/folder counts
 * Immediately show new chat room tab with no delay
 * Show message in chat room tab if joining a private room is not successful
 * Automatically resize panes and certain columns when window size changes
 * Finding in tree view lists now searches data in all columns
 * Enabled caret navigation for chat view screen reading and improved chat entry focusing when paging up and down
 * Only open the listening port when connecting to the server
 * Several fixes related to inconsistent behavior when banning or ignoring users/IP addresses
 * Several fixes related to accessibility
 * Windows/macOS: Fixed chat emoji rendering
 * Windows: Stop using 'portable' term for standalone packages
 * macOS: Fixed laggy list scrolling and window resizing

### Issues closed on GitHub

 * Sort by speed ([#373](https://github.com/nicotine-plus/nicotine-plus/issues/373))
 * Bind Nicotine+ to specified network adapter ([#871](https://github.com/nicotine-plus/nicotine-plus/issues/871))
 * Finish running transfers and quit ([#885](https://github.com/nicotine-plus/nicotine-plus/issues/885))
 * Implement search request delivery to child peers ([#994](https://github.com/nicotine-plus/nicotine-plus/issues/994))
 * Improvement ideas for the search result filters ([#1400](https://github.com/nicotine-plus/nicotine-plus/issues/1400))
 * Force download a filtered file ([#1419](https://github.com/nicotine-plus/nicotine-plus/issues/1419))
 * Reopen closed tabs ([#1424](https://github.com/nicotine-plus/nicotine-plus/issues/1424))
 * Anyone willing to maintain an official Nicotine+ Debian package? ([#1448](https://github.com/nicotine-plus/nicotine-plus/issues/1448))
 * M1 Mac support? ([#1475](https://github.com/nicotine-plus/nicotine-plus/issues/1475))
 * Show list of logged private chat users ([#1509](https://github.com/nicotine-plus/nicotine-plus/issues/1509))
 * List of GTK 4 regressions ([#1554](https://github.com/nicotine-plus/nicotine-plus/issues/1554))
 * Crashes when sending emoji ([#1556](https://github.com/nicotine-plus/nicotine-plus/issues/1556))
 * Leech Detector is bugging people who have folders shared already. ([#1565](https://github.com/nicotine-plus/nicotine-plus/issues/1565))
 * Get date in transfer total up/dl statistic ([#1598](https://github.com/nicotine-plus/nicotine-plus/issues/1598))
 * Determine the size etc of a folder / selected files ([#1628](https://github.com/nicotine-plus/nicotine-plus/issues/1628))
 * Warning if no files are shared ([#1698](https://github.com/nicotine-plus/nicotine-plus/issues/1698))
 * Filter for song length ([#1727](https://github.com/nicotine-plus/nicotine-plus/issues/1727))
 * Split log file on certain file size threshold? ([#1758](https://github.com/nicotine-plus/nicotine-plus/issues/1758))
 * An option to silently run command when a download is finished ([#1847](https://github.com/nicotine-plus/nicotine-plus/issues/1847))
 * Mass PM ([#1860](https://github.com/nicotine-plus/nicotine-plus/issues/1860))
 * Show files to all but locked ([#1870](https://github.com/nicotine-plus/nicotine-plus/issues/1870))
 * Bumping minimum version requirements for Python and GTK 3 ([#1871](https://github.com/nicotine-plus/nicotine-plus/issues/1871))
 * \[3.3.0.dev1\] After rescan complete, No GUI just crashes python 3.10.2 errors? ([#1915](https://github.com/nicotine-plus/nicotine-plus/issues/1915))
 * I need file sizes to be displayed in bytes, not interested in abbreviated MiB sizing. ([#1948](https://github.com/nicotine-plus/nicotine-plus/issues/1948))
 * Turn the ✉ blue, instead of adding a blue dot. ([#1954](https://github.com/nicotine-plus/nicotine-plus/issues/1954))
 * Gdk-CRITICAL messages related to tray icon ([#1973](https://github.com/nicotine-plus/nicotine-plus/issues/1973))
 * \[3.3.0.dev1\] Breakage on latest master ([#1982](https://github.com/nicotine-plus/nicotine-plus/issues/1982))
 * Add toggles for global upload/download speed limits to the status bar ([#1987](https://github.com/nicotine-plus/nicotine-plus/issues/1987))
 * \[3.3.0.dev1\] Critical error dialog on start up ([#1989](https://github.com/nicotine-plus/nicotine-plus/issues/1989))
 * \[3.3.0.dev1\] Critical error on file transfer if not looking at tab ([#1994](https://github.com/nicotine-plus/nicotine-plus/issues/1994))
 * Chat rooms go out of order and names disappear and walls seem inaccessible ([#2003](https://github.com/nicotine-plus/nicotine-plus/issues/2003))
 * \[3.3.0.dev1\] Flashing Window ([#2010](https://github.com/nicotine-plus/nicotine-plus/issues/2010))
 * \[3.3.0.dev1\] Value: argument child: Expected Gtk.Widget, but got str ([#2021](https://github.com/nicotine-plus/nicotine-plus/issues/2021))
 * Nicotine+ listening on port before manually connecting ([#2025](https://github.com/nicotine-plus/nicotine-plus/issues/2025))
 * Make log history font configurable ([#2074](https://github.com/nicotine-plus/nicotine-plus/issues/2074))
 * Feature: Provide a list of all open chat and chat room tabs ([#2079](https://github.com/nicotine-plus/nicotine-plus/issues/2079))
 * Clear deleted files ([#2084](https://github.com/nicotine-plus/nicotine-plus/issues/2084))
 * Granular control over shares with trusted buddies (+ custom buddy shares?) ([#2093](https://github.com/nicotine-plus/nicotine-plus/issues/2093))
 * Let other users know the minimum number of files and folders set in the Leech Detector plugin ([#2103](https://github.com/nicotine-plus/nicotine-plus/issues/2103))
 * Save leechers persistently ([#2105](https://github.com/nicotine-plus/nicotine-plus/issues/2105))
 * Easier way to remove ban from a user ([#2111](https://github.com/nicotine-plus/nicotine-plus/issues/2111))
 * \[3.3.0.dev1\] Tray icon has disappeared in the latest version ([#2113](https://github.com/nicotine-plus/nicotine-plus/issues/2113))
 * \[3.3.0.dev1\] Critical error (UI window with bug report) ([#2116](https://github.com/nicotine-plus/nicotine-plus/issues/2116))
 * Option to choose language in Nicotine+ ([#2134](https://github.com/nicotine-plus/nicotine-plus/issues/2134))
 * Bitrate filter does not work as expected ([#2141](https://github.com/nicotine-plus/nicotine-plus/issues/2141))
 * Random hanging + zombie process on MacOS with VPN and Little Snitch ([#2154](https://github.com/nicotine-plus/nicotine-plus/issues/2154))
 * Chat emoji scaling issue ([#2169](https://github.com/nicotine-plus/nicotine-plus/issues/2169))
 * Remember last sorted column for each tab (Downloads, Uploads, Search Files, etc) ([#2170](https://github.com/nicotine-plus/nicotine-plus/issues/2170))
 * Window resizing glitchy on MacOS 12.1 ([#2178](https://github.com/nicotine-plus/nicotine-plus/issues/2178))
 * \[3.3.0.dev3\] Unstable Windows builds fail to start due to missing .dll ([#2218](https://github.com/nicotine-plus/nicotine-plus/issues/2218))
 * Notifications for wish list results ([#2221](https://github.com/nicotine-plus/nicotine-plus/issues/2221))
 * Save wishlists automatically after closing the corresponding window ([#2249](https://github.com/nicotine-plus/nicotine-plus/issues/2249))
 * In the downloads tab, filter by filename ([#2251](https://github.com/nicotine-plus/nicotine-plus/issues/2251))
 * \[3.3.0.dev3\] Removing a second user from the buddy list makes nicotine crash ([#2252](https://github.com/nicotine-plus/nicotine-plus/issues/2252))
 * \[3.3.0.dev3\] Tray icon changing while nicotine minimized causing crashes ([#2258](https://github.com/nicotine-plus/nicotine-plus/issues/2258))
 * Nicotine+ split-tunneling connection to server issue ([#2285](https://github.com/nicotine-plus/nicotine-plus/issues/2285))
 * Error launching ([#2290](https://github.com/nicotine-plus/nicotine-plus/issues/2290))
 * Add sortable audio properties/quality column ([#2296](https://github.com/nicotine-plus/nicotine-plus/issues/2296))
 * \[3.3.0.dev4\] macOS: jumpy window with straight corners and unresizable ([#2298](https://github.com/nicotine-plus/nicotine-plus/issues/2298))
 * Add dates to statistics dialog ([#2316](https://github.com/nicotine-plus/nicotine-plus/issues/2316))
 * \[3.3.0.dev4\] Nicotine crashes on launch ([#2320](https://github.com/nicotine-plus/nicotine-plus/issues/2320))
 * "Add to Buddy List" button in User Info should be greyed/disabled out if already on Buddy List ([#2325](https://github.com/nicotine-plus/nicotine-plus/issues/2325))
 * \[3.3.0.dev4\] Nicotine+ crashes some time after launch ([#2341](https://github.com/nicotine-plus/nicotine-plus/issues/2341))
 * \[3.3.0.dev4\] Unusual CPU usage ([#2361](https://github.com/nicotine-plus/nicotine-plus/issues/2361))
 * \[3.3.0.dev4\] Crash upon download start ([#2391](https://github.com/nicotine-plus/nicotine-plus/issues/2391))
 * Upnp Port does not close upon exit of nicotine+ ([#2393](https://github.com/nicotine-plus/nicotine-plus/issues/2393))
 * \[3.3.0.dev4\] Critical error after clicking "close" button in "Transfer statistics" ([#2394](https://github.com/nicotine-plus/nicotine-plus/issues/2394))
 * Visit my own user profile ([#2412](https://github.com/nicotine-plus/nicotine-plus/issues/2412))
 * \[3.3.0.dev4\] Critical error upon opening File Properties of search results ([#2415](https://github.com/nicotine-plus/nicotine-plus/issues/2415))
 * \[3.3.0.dev4\] Crash on startup ([#2439](https://github.com/nicotine-plus/nicotine-plus/issues/2439))
 * \[3.3.0.dev4\] Nicotine crash on many downloads, all folder downloads. ([#2446](https://github.com/nicotine-plus/nicotine-plus/issues/2446))
 * Uploads erroneously getting listed as complete, actually "aborted" at 99% ([#2447](https://github.com/nicotine-plus/nicotine-plus/issues/2447))
 * Very strange bug with program interface ([#2448](https://github.com/nicotine-plus/nicotine-plus/issues/2448))
 * Date format in buddy list ([#2450](https://github.com/nicotine-plus/nicotine-plus/issues/2450))
 * \[3.3.0.dev4\] Fatal run-time error involving file descriptors ([#2451](https://github.com/nicotine-plus/nicotine-plus/issues/2451))
 * Show list of logged private chat users ([#2469](https://github.com/nicotine-plus/nicotine-plus/issues/2469))
 * \[3.3.0.dev3\] Gtk.CssProvider crashes Nicotine 3.3.0.dev3 at startup ([#2474](https://github.com/nicotine-plus/nicotine-plus/issues/2474))
 * Closing Nicotine as a background app on Gnome 44 ([#2487](https://github.com/nicotine-plus/nicotine-plus/issues/2487))
 * Rejoin rooms in order ([#2490](https://github.com/nicotine-plus/nicotine-plus/issues/2490))
 * Turn off display of automatic chat messages ([#2510](https://github.com/nicotine-plus/nicotine-plus/issues/2510))
 * Unable to Connect to SoulSeek Server when Dual Network Interface Is Configured ([#2518](https://github.com/nicotine-plus/nicotine-plus/issues/2518))
 * Search filter: username ([#2537](https://github.com/nicotine-plus/nicotine-plus/issues/2537))
 * Wishlist results - sound alert and flashing icon when minimized ([#2551](https://github.com/nicotine-plus/nicotine-plus/issues/2551))
 * Default image viewer ([#2552](https://github.com/nicotine-plus/nicotine-plus/issues/2552))
 * Auto resume/retry ([#2555](https://github.com/nicotine-plus/nicotine-plus/issues/2555))
 * RecursionError: maximum recursion depth exceeded while calling a Python object when trying to share files ([#2560](https://github.com/nicotine-plus/nicotine-plus/issues/2560))
 * \[3.3.0.dev5\] Crash ([#2566](https://github.com/nicotine-plus/nicotine-plus/issues/2566))
 * Downloads appearing in the "received" folder ([#2568](https://github.com/nicotine-plus/nicotine-plus/issues/2568))
 * UnicodeEncodeError ([#2569](https://github.com/nicotine-plus/nicotine-plus/issues/2569))
 * \[3.3.0.dev5\] Crash (maybe before network reconnect, not sure) ([#2573](https://github.com/nicotine-plus/nicotine-plus/issues/2573))
 * \[3.3.0.dev5\] Couldn't remember the password for one of my usernames, crashed when i tried to change login ([#2582](https://github.com/nicotine-plus/nicotine-plus/issues/2582))
 * Its not possible to set download folders when they are already set to invalid drive ([#2586](https://github.com/nicotine-plus/nicotine-plus/issues/2586))
 * \[3.3.0.dev5\] N+ crashes on startup on macos 13.4.1 ([#2587](https://github.com/nicotine-plus/nicotine-plus/issues/2587))
 * Nicotine+ Low FPS/Stuttering on Mac OS ([#2589](https://github.com/nicotine-plus/nicotine-plus/issues/2589))
 * Log function not working ([#2591](https://github.com/nicotine-plus/nicotine-plus/issues/2591))
 * \[3.3.0.dev5\] Download does not seem to work ([#2595](https://github.com/nicotine-plus/nicotine-plus/issues/2595))
 * \[3.3.0.dev5\] Share scanning process not working in Windows and macOS builds ([#2608](https://github.com/nicotine-plus/nicotine-plus/issues/2608))
 * \[3.3.0.dev5\] Error message whilst exiting n+ ([#2610](https://github.com/nicotine-plus/nicotine-plus/issues/2610))
 * \[3.3.0.dev5\] Clicking Clear All > Finished or User Actions > Send Message doesn't do anything. ([#2617](https://github.com/nicotine-plus/nicotine-plus/issues/2617))
 * \[3.3.0.dev5\] Nicotine silently crashes/exits when disconnecting external monitor ([#2627](https://github.com/nicotine-plus/nicotine-plus/issues/2627))
 * \[3.3.0.dev5\] When typing in "Include text" box and hitting enter, Nicotine runs into a critical error ([#2628](https://github.com/nicotine-plus/nicotine-plus/issues/2628))
 * \[3.3.0.dev5\] Nicotine+ App won't open ([#2638](https://github.com/nicotine-plus/nicotine-plus/issues/2638))
 * Read-only editfields aren't read by Orca screen-reader correctly ([#2647](https://github.com/nicotine-plus/nicotine-plus/issues/2647))
 * Enable GTK3 while running Orca by default ([#2652](https://github.com/nicotine-plus/nicotine-plus/issues/2652))
 * \[3.3.0.dev5\] Crash on the Upload window ([#2663](https://github.com/nicotine-plus/nicotine-plus/issues/2663))
 * \[3.3.0.dev5\] Gtk:ERROR:../gtk/gtk/deprecated/gtktreeview.c:12838:gtk\_tree\_view\_is\_blank\_at\_pos: code should not be reached ([#2665](https://github.com/nicotine-plus/nicotine-plus/issues/2665))
 * Download folder for remote user keeps appearing ([#2667](https://github.com/nicotine-plus/nicotine-plus/issues/2667))
 * Can you swap "close" and "reset" buttons? ([#2678](https://github.com/nicotine-plus/nicotine-plus/issues/2678))
 * \[3.3.0.dev6\] Crashing when uploading folders to user ([#2690](https://github.com/nicotine-plus/nicotine-plus/issues/2690))
 * PORT Issue! ([#2694](https://github.com/nicotine-plus/nicotine-plus/issues/2694))
 * Show total folder size on search tab ([#2697](https://github.com/nicotine-plus/nicotine-plus/issues/2697))
 * Nicotine+ freezes for minutes at a time ([#2700](https://github.com/nicotine-plus/nicotine-plus/issues/2700))
 * Remove "Send To Player" from main right-click menu ([#2705](https://github.com/nicotine-plus/nicotine-plus/issues/2705))
 * Make banning user stop them from viewing profile ([#2710](https://github.com/nicotine-plus/nicotine-plus/issues/2710))
 * \[3.3.0.dev6\] Nicotine crashing ([#2713](https://github.com/nicotine-plus/nicotine-plus/issues/2713))
 * \[3.3.0.dev6\] Some 3.3.0.dev6 issues ([#2714](https://github.com/nicotine-plus/nicotine-plus/issues/2714))
 * \[3.3.0.dev6\] Clicking "Clear Finished" crashes (sometimes) ([#2729](https://github.com/nicotine-plus/nicotine-plus/issues/2729))
 * \[3.3.0.dev6\] Crash on master updating completion from "user_left_room" ([#2733](https://github.com/nicotine-plus/nicotine-plus/issues/2733))
 * \[3.3.0.dev6\] Crash on DL tab CLEAR files right-click option ([#2745](https://github.com/nicotine-plus/nicotine-plus/issues/2745))
 * \[3.3.0.dev6\] Private chat: messages showing with wrong sender ([#2755](https://github.com/nicotine-plus/nicotine-plus/issues/2755))
 * Ability to set default Buddies tab list sort ([#2758](https://github.com/nicotine-plus/nicotine-plus/issues/2758))
 * UI/UX improvement: move the buddies only option out of the edit subwindow to the share window ([#2763](https://github.com/nicotine-plus/nicotine-plus/issues/2763))
 * Critical Error: UnicodeEncodeError ([#2767](https://github.com/nicotine-plus/nicotine-plus/issues/2767))
 * "Invisible Border" Around Program? ([#2768](https://github.com/nicotine-plus/nicotine-plus/issues/2768))
 * Launching 25-NOV Build Causes Frequent & Prolonged Freezing Of Win10 OS+Frequent Disconnects ([#2770](https://github.com/nicotine-plus/nicotine-plus/issues/2770))
 * No handler for class \<class 'pynicotine.slskmessages.UserLeftRoom'\> ([#2771](https://github.com/nicotine-plus/nicotine-plus/issues/2771))
 * \[3.3.0.dev6\] Network connectivity lost until a server reconnect ([#2778](https://github.com/nicotine-plus/nicotine-plus/issues/2778))
 * \[3.3.0.dev6\] Copying search result filenames causes crash ([#2781](https://github.com/nicotine-plus/nicotine-plus/issues/2781))
 * Recursive folder download matches extra siblings starting with the same name ([#2782](https://github.com/nicotine-plus/nicotine-plus/issues/2782))
 * Critical 'TypeError' on macOS Monterey, N+ won't launch ([#2785](https://github.com/nicotine-plus/nicotine-plus/issues/2785))
 * \[3.3.0rc1\] "Unknown search mode" Reopening a whishlist search tab ([#2798](https://github.com/nicotine-plus/nicotine-plus/issues/2798))
 * Right clicking into the search bar or ctrl+v copy paste causes application to crash ([#2809](https://github.com/nicotine-plus/nicotine-plus/issues/2809))
 * Browse Shares: folder downloads should always be recursive ([#2812](https://github.com/nicotine-plus/nicotine-plus/issues/2812))
 * \[3.3.0rc2\] Some event causes text copied to clipboard outside Nicotine+ to be ignored ([#2815](https://github.com/nicotine-plus/nicotine-plus/issues/2815))
 * Change search share behavior to classic Soulseek ([#2819](https://github.com/nicotine-plus/nicotine-plus/issues/2819))
 * Sudden stop while selecting 'grey' files to download ([#2820](https://github.com/nicotine-plus/nicotine-plus/issues/2820))
 * Classic Soulseek re-enter search function ([#2826](https://github.com/nicotine-plus/nicotine-plus/issues/2826))
 * N+ 3.3.0 transfers not working ([#2827](https://github.com/nicotine-plus/nicotine-plus/issues/2827))
 * "Browse Files" doesn't always work on the first try ([#2829](https://github.com/nicotine-plus/nicotine-plus/issues/2829))
 * \[3.3.0rc2\] Disable sorting in search ([#2830](https://github.com/nicotine-plus/nicotine-plus/issues/2830))
 * Notification on new results from wishlist ([#2840](https://github.com/nicotine-plus/nicotine-plus/issues/2840))
 * \[3.3.0rc3\] SVG icons not shown ([#2841](https://github.com/nicotine-plus/nicotine-plus/issues/2841))
 * \[3.3.0rc3\] Instant crash with Nicotine+ 3.3.0-rc3 with Apple Silicon image ([#2842](https://github.com/nicotine-plus/nicotine-plus/issues/2842))
 * \[3.3.0rc3\] Styling of contextual menu in higlighted tabs ([#2845](https://github.com/nicotine-plus/nicotine-plus/issues/2845))


## Version 3.2.9 (March 5, 2023)

### Corrections

 * Reduced memory usage when browsing large shares
 * Fixed a crash on some systems after running for a few days
 * Fixed an issue where some private messages were ignored after a user reconnected
 * Fixed an issue where downloads with long file names could fail on eCryptfs file systems
 * Fixed an issue where the displayed total percentage of folder transfers was incorrect
 * Fixed an issue where the tray icon could disappear after locking the screen

### Issues closed on GitHub

 * Messages are wonky ([#2329](https://github.com/nicotine-plus/nicotine-plus/issues/2329))
 * Current download progress reflects single download instead of total ([#2373](https://github.com/nicotine-plus/nicotine-plus/issues/2373))
 * Download I/O error: \[Errno 36\] File name too long ([#2375](https://github.com/nicotine-plus/nicotine-plus/issues/2375))


## Version 3.2.8 (January 6, 2023)

### Corrections

 * Improved file scanning performance on systems other than Windows
 * Fixed a regression where uploads through the legacy file transfer system failed in some cases
 * Fixed an issue where finished zero-byte file downloads displayed a "Connection timeout" error
 * Fixed an issue where Nicotine+ did not reconnect to the server on connection failure in some cases
 * Fixed a rare crash when scanning shares
 * Windows: Fixed a crash when sending Nicotine+ to the background from the quit confirmation dialog
 * Windows: Fixed an issue that prevented viewing own personal user info page

### Issues closed on GitHub

 * Automatically reconnect to a server after connection failure ([#2168](https://github.com/nicotine-plus/nicotine-plus/issues/2168))
 * Nicotine+ v3.2.7 crashes when sent to background (Windows 10) ([#2276](https://github.com/nicotine-plus/nicotine-plus/issues/2276))
 * Error launching Nicotine+ ([#2282](https://github.com/nicotine-plus/nicotine-plus/issues/2282))
 * UPnP: Critical error when network interface not available ([#2289](https://github.com/nicotine-plus/nicotine-plus/issues/2289))


## Version 3.2.7 (December 1, 2022)

### Corrections

 * Fixed a crash when selecting a user picture
 * Fixed a crash when removing private chat logs
 * Fixed an issue where the main window could become unresponsive when showing it from the tray icon
 * Minor fixes related to UPnP compatibility with certain routers
 * Reduce the number of connection timeouts when searching for popular files
 * Windows: Fixed a possible crash when showing notification bubbles
 * Android (Termux): Fixed a crash when starting Nicotine+ in headless mode

### Issues closed on GitHub

 * Notification string too long (ValueError crash) on Windows ([#2233](https://github.com/nicotine-plus/nicotine-plus/issues/2233))
 * Private chat, Delete chat log... >> Value: 'PrivateChats' object has no attribute 'history' ([#2247](https://github.com/nicotine-plus/nicotine-plus/issues/2247))
 * Flatpak: uploading a profile picture crashes the application ([#2250](https://github.com/nicotine-plus/nicotine-plus/issues/2250))


## Version 3.2.6 (October 21, 2022)

### Changes

 * Added F6 shortcut to move keyboard focus to the headerbar/toolbar
 * Added an option to clear all uploads with a "User logged off" status
 * Removed AppIndicator dependency in favor of custom tray icon implementation

### Corrections

 * IMPORTANT: Fixed a regression where uploads to slskd users were stuck at "Transferring"
 * IMPORTANT: Fixed an issue where private messages from offline users were ignored
 * IMPORTANT: Fixed an issue where certain uploads were incorrectly marked as "Cancelled"
 * IMPORTANT - OpenBSD: Fixed a regression where incoming peer connections did not work
 * Fixed a crash when uploading large files on a 32-bit system
 * Fixed an issue where redundant protocol messages could be sent to the server indefinitely
 * Fixed an issue where UPnP did not work on MikroTik routers
 * Fixed an issue where the progress bar would get stuck if a share browse request ended abruptly
 * Windows: Fixed an issue where network drives could not be shared
 * Flatpak: Fixed an issue where the GUI was not translated to the system language

### Issues closed on GitHub

 * Clear Finished also clears uploads/downloads with "User logged off" status ([#2081](https://github.com/nicotine-plus/nicotine-plus/issues/2081))
 * Scanning taking many hours ([#2173](https://github.com/nicotine-plus/nicotine-plus/issues/2173))
 * Users can't connect to me after upgrade to 3.2.5 (transfers don't work) on OpenBSD ([#2175](https://github.com/nicotine-plus/nicotine-plus/issues/2175))
 * Some bugs in Nicotine+ v. 3.2.5 ([#2184](https://github.com/nicotine-plus/nicotine-plus/issues/2184))
 * Search Files: Keyboard shortcut to focus search bar ([#2186](https://github.com/nicotine-plus/nicotine-plus/issues/2186))
 * Offline messages not popping up in tabs ([#2189](https://github.com/nicotine-plus/nicotine-plus/issues/2189))
 * Samba Share hosted by Linux, mounted on Windows Failing ([#2190](https://github.com/nicotine-plus/nicotine-plus/issues/2190))
 * Can't exit Room tabs when internet connection is off ([#2192](https://github.com/nicotine-plus/nicotine-plus/issues/2192))
 * The flatpak version of Nicotine+ is using the wrong language ([#2194](https://github.com/nicotine-plus/nicotine-plus/issues/2194))
 * Uploads partly broken ([#2197](https://github.com/nicotine-plus/nicotine-plus/issues/2197))
 * Error code 725: OnlyPermanentLeasesSupported ([#2200](https://github.com/nicotine-plus/nicotine-plus/issues/2200))
 * Critical error ([#2215](https://github.com/nicotine-plus/nicotine-plus/issues/2215))
 * OverflowError ([#2216](https://github.com/nicotine-plus/nicotine-plus/issues/2216))


## Version 3.2.5 (August 31, 2022)

### Corrections

 * Fixed an issue where user settings would reset after an operating system crash or power outage
 * Fixed an issue where certain uploads were stuck in "Queued" or "Transferring" status
 * Fixed an issue where files did not download to custom folders
 * Fixed a performance regression when loading downloads/uploads on startup
 * Fixed an issue where Nicotine+ connected to the server before UPnP port forwarding completed
 * Fixed a rare crash related to peer connections
 * Fixed a crash when an invalid debug log folder was set
 * Windows: Fixed a regression in scrolling and text rendering performance

### Issues closed on GitHub

 * Settings are reset to application defaults when a system crash occurs ([#2147](https://github.com/nicotine-plus/nicotine-plus/issues/2147))
 * Critical Error ([#2148](https://github.com/nicotine-plus/nicotine-plus/issues/2148))
 * 3.2.4 performs worse on Windows than previous stable version (3.2.2) ([#2150](https://github.com/nicotine-plus/nicotine-plus/issues/2150))
 * Left unattended just crashed on win 11 beta slow ring ([#2151](https://github.com/nicotine-plus/nicotine-plus/issues/2151))


## Version 3.2.4 (August 7, 2022)

### Corrections

 * Fixed a regression where shared folders could not be added using the Preferences dialog
 * Fixed a performance regression when updating file transfer lists
 * Fixed a potential crash when displaying the estimated time of a very large download

### Issues closed on GitHub

 * File sharing error ([#2142](https://github.com/nicotine-plus/nicotine-plus/issues/2142))


## Version 3.2.3 (August 5, 2022)

### Changes

 * Optimized performance when many shared files and file transfers are present
 * Implemented mouse wheel scrolling on tabs to change the active page
 * Search results from ignored users are no longer shown
 * Added total file size and duration of selected files to the File Properties dialog
 * Added text-to-speech toggle buttons for individual private chats when TTS is enabled
 * Usability improvements to several main window components and dialogs
 * Reddit and Test Replier plugins are no longer included by default, moved to examplars on [GitHub](https://github.com/nicotine-plus/nicotine-plus/tree/HEAD/pynicotine/plugins/examplars)
 * Various translation updates (thanks to our [many contributors](https://nicotine-plus.org/AUTHORS#translators) on [Weblate](https://hosted.weblate.org/engage/nicotine-plus))

### Corrections

 * IMPORTANT: Fixed a CPU hogging issue when thousands of file transfers were present
 * Fixed issues where downloads failed if the path or file name was very long (thank you @AtticFinder65536)
 * Fixed an issue where folder downloads did not always save subfolders into the correct location
 * Fixed an issue where the estimated total time remaining for folder transfers was incorrect
 * Fixed an issue where clearing all file transfers did not remove transfers completely
 * Fixed a rare crash when downloading files onto certain (latin-1) filesystems
 * Fixed a discrepancy between the upload speed reported in outgoing search results compared to user info
 * Fixed an issue where dark mode was used when light mode was enabled on some systems
 * Unmaximized size of the main window is now remembered after the window is maximized
 * Reduced memory usage after closing search tabs with many results
 * Flatpak: network folders can now be shared
 * Various minor bug fixes

### Issues closed on GitHub

 * Forcibly re-queue uploads that stop due to an error such as "Can't connect" ([#1563](https://github.com/nicotine-plus/nicotine-plus/issues/1563))
 * Support paths longer than 260 characters on Windows ([#1728](https://github.com/nicotine-plus/nicotine-plus/issues/1728))
 * UnicodeEncodeError when downloading file ([#1980](https://github.com/nicotine-plus/nicotine-plus/issues/1980))
 * Nicotine+ always on dark mode regardless of my settings ([#1983](https://github.com/nicotine-plus/nicotine-plus/issues/1983))
 * High CPU Usage pegs a single core ([#1998](https://github.com/nicotine-plus/nicotine-plus/issues/1998))
 * Weird behavior when I download a whole folder with multiple subdirectories ([#2004](https://github.com/nicotine-plus/nicotine-plus/issues/2004))
 * Don't freeze/crash without xdg-open ([#2005](https://github.com/nicotine-plus/nicotine-plus/issues/2005))
 * Unicode encode error ([#2015](https://github.com/nicotine-plus/nicotine-plus/issues/2015))
 * Russian translation updated ([#2016](https://github.com/nicotine-plus/nicotine-plus/issues/2016))
 * Time Left for folder and user same as for currently active file ([#2018](https://github.com/nicotine-plus/nicotine-plus/issues/2018))
 * Time Left column regression ([#2020](https://github.com/nicotine-plus/nicotine-plus/issues/2020))
 * Clear ALL downloads, Clear ALL uploads not working ([#2023](https://github.com/nicotine-plus/nicotine-plus/issues/2023))
 * User note saves when pressing Cancel ([#2036](https://github.com/nicotine-plus/nicotine-plus/issues/2036))
 * Please show completed transfer speeds in the upload tab. ([#2082](https://github.com/nicotine-plus/nicotine-plus/issues/2082))
 * Column headings overlapping in the downloads tab ([#2090](https://github.com/nicotine-plus/nicotine-plus/issues/2090))
 * Sort similar users by interest ([#2096](https://github.com/nicotine-plus/nicotine-plus/issues/2096))
 * Change the cursor to a finger when it's over links ([#2101](https://github.com/nicotine-plus/nicotine-plus/issues/2101))
 * \[3.2.3.rc2\] Critical error (UI window with bug report) ([#2116](https://github.com/nicotine-plus/nicotine-plus/issues/2116))
 * Lists of shared files not human-readable ([#2118](https://github.com/nicotine-plus/nicotine-plus/issues/2118))
 * \[3.2.3.rc2\] Exception thrown when highlighting several uploads & selecting "Clear" ([#2124](https://github.com/nicotine-plus/nicotine-plus/issues/2124))

## Version 3.2.2 (March 19, 2022)

### Changes

 * Show file size in bytes in addition to factorized size in the File Properties dialog
 * Disallow setting listening ports below 1024, which is in the operating system privileged range
 * /exit /quit and /q commands respect the 'When closing Nicotine+' preference
 * Prevent visual lag in chats by displaying new messages in the GUI before writing them into the log file
 * Simplify the Public room feed layout and mention the actual room name in text-to-speech messages
 * Check whole words for username mentions in chat rooms to avoid raising notifications for subwords

### Corrections

 * IMPORTANT: Prevent random upload timeouts of large files if the remote user has a slow or limited download speed
 * Incomplete downloads are restarted if the file contents change on the uploader's end
 * Fixed a regression where users could not be added to private rooms
 * Fixed a regression where certain uploads could fail with a 'Cannot connect' status
 * Fixed an issue which prevented uploads slots from opening while a privileged transfer was in progress
 * Fixed a race condition where previously queued uploads were wrongly denied during rescan on startup
 * Fixed a rare issue where a download could restart endlessly if the file is unreadable on the uploader's end
 * Fixed a rare crash when loading stored downloads that contain erroneous filename data
 * Fixed broken folder structure when downloading folders containing multiple levels of subfolders
 * Fixed a crash loop if a text-to-speech message with an invalid syntax is set
 * Fixed an issue where ban messages could not be sent to a user with a banned IP address
 * Fixed an issue where folder names could not be copied with the Ctrl+C shortcut
 * Fixed a rare crash when changing the color of tab labels
 * Fixed the behaviour of auto-away messages which are now sent as often as required and displayed locally
 * Fixed an issue that prevented automatic column width sizing when double clicking column separators
 * Fixed the sort order of the Time Elapsed and Time Remaining columns in the Downloads and Uploads views

### Issues closed on GitHub

 * Chat mentions with 1 character username ([#1790](https://github.com/nicotine-plus/nicotine-plus/issues/1790))
 * Sort order time elapsed is off for uploads over an hour ([#1795](https://github.com/nicotine-plus/nicotine-plus/issues/1795))
 * Just crashed on windows insider 11 slow ring ([#1875](https://github.com/nicotine-plus/nicotine-plus/issues/1875))
 * Translations Bug when Autoconnect is off ([#1884](https://github.com/nicotine-plus/nicotine-plus/issues/1884))
 * Crash (Gtk tab color) ([#1889](https://github.com/nicotine-plus/nicotine-plus/issues/1889))
 * Auto Size Column Does Not Fit Username, Folder or Filename ([#1901](https://github.com/nicotine-plus/nicotine-plus/issues/1901))
 * Transfers Cancelling Randomly ([#1911](https://github.com/nicotine-plus/nicotine-plus/issues/1911))
 * Nicotine+ doesn't open: Value: 'int' object has no attribute 'split' error ([#1917](https://github.com/nicotine-plus/nicotine-plus/issues/1917))
 * Upload Slots Not Opening ([#1933](https://github.com/nicotine-plus/nicotine-plus/issues/1933))
 * Departure during the copy action Nicotine+ 3.3.0.dev1 ([#1938](https://github.com/nicotine-plus/nicotine-plus/issues/1938))
 * Note editing no longer opens by double-clicking? 3.3.0.dev1 ([#1939](https://github.com/nicotine-plus/nicotine-plus/issues/1939))
 * Nicotine+ does not preserve the folder structure when downloading ([#1940](https://github.com/nicotine-plus/nicotine-plus/issues/1940))


## Version 3.2.1 (February 10, 2022)

### Changes

 * Optimized overall performance and stability related to Soulseek server and peer connections
 * Optimized performance and improve robustness of the round robin queue system (thank you @toofar)
 * Optimized scrolling performance and avoid FPS drops when scrolling large lists containing country flags
 * Optimized parent row expansions when adding new search results and transfers into tree views
 * Optimized loading performance of downloads/uploads history and avoid unnecessary saving of transfer lists
 * Optimized loading performance and reduce memory usage of open chat tabs
 * Optimized connection initialization performance when uploading to certain users
 * Changed the chat log filename replacement character from - to _ in room names containing an illegal character
 * Changed display of items in the Uploads transfer list to virtual folder paths instead of local folder paths
 * Added display of local folder paths for local items in the File Properties dialog
 * Added direct folder and file browsing with slsk:// URLs in the Browse Shares text entry
 * Added new Ukrainian translation (thank you @uniss2209)
 * Lots of updates to the translations (thanks to our [many contributors](https://nicotine-plus.org/AUTHORS#translators) on [Weblate](https://hosted.weblate.org/engage/nicotine-plus))

### Corrections

 * CRITICAL: Fixed a crash vulnerability when receiving a download request with a malformed file path (affects version 3.0.3 and later)
 * IMPORTANT: Fixed an issue where uploads could become stuck in the transfer queue forever
 * IMPORTANT: Fixed an issue where language translations were not automatically applied on Windows and macOS
 * Fixed a regression where pausing a download doesn't actually pause it if translations are used
 * Fixed an issue where downloads failed to start if the temporary incomplete filename is more than 255 characters
 * Fixed an issue where paused downloads started downloading in a random order when resumed
 * Fixed a regression where the bandwidth status indicator failed to update if the transfers tab was inactive
 * Fixed broken scrollbar when changing active page in the Preferences dialog
 * Fixed labels of UI elements in the Russian translation (thank you @SnIPeRSnIPeR)

### Issues closed on GitHub

 * After using Clear on an uploaded item, it gets removed, but then returns ([#1745](https://github.com/nicotine-plus/nicotine-plus/issues/1745))
 * Direct Connection Fails ([#1748](https://github.com/nicotine-plus/nicotine-plus/issues/1748))
 * I cannot see my profile info and picture like I am able to on other user's profiles ([#1751](https://github.com/nicotine-plus/nicotine-plus/issues/1751))
 * All file paths are reversed (e.g. /home/foo/Downloads -> /Downloads/foo/home/) ([#1759](https://github.com/nicotine-plus/nicotine-plus/issues/1759))
 * Logs mention "privileged" users not "prioritized" users ([#1764](https://github.com/nicotine-plus/nicotine-plus/issues/1764))
 * Add an option to print full paths relatively to their share ([#1775](https://github.com/nicotine-plus/nicotine-plus/issues/1775))
 * Can't connect to soulseek network - specified ports unusable (Windows 11) ([#1778](https://github.com/nicotine-plus/nicotine-plus/issues/1778))
 * Windows 11: \[3.1.1\] Just crashed on Win 11 insider ring ([#1777](https://github.com/nicotine-plus/nicotine-plus/issues/1777))
 * \[3.2.0.dev1\] Unknown config option 'show_private_results' ([#1779](https://github.com/nicotine-plus/nicotine-plus/issues/1779))
 * \[3.2.1.dev1\] Crash on adding user to buddy list ([#1792](https://github.com/nicotine-plus/nicotine-plus/issues/1792))
 * Windows/macOS: Can't change language in app ([#1796](https://github.com/nicotine-plus/nicotine-plus/issues/1796))
 * \[3.2.1.dev1\] Occasional crash ([#1798](https://github.com/nicotine-plus/nicotine-plus/issues/1798))
 * \[3.2.1.dev1\] Country_Code related Critical Error since update to Mint 20.3 ([#1806](https://github.com/nicotine-plus/nicotine-plus/issues/1806))
 * Increase network speed update time ([#1817](https://github.com/nicotine-plus/nicotine-plus/issues/1817))
 * \[3.2.1.dev1\] GTK 4: Closing private chat tab can crash Nicotine+ ([#1821](https://github.com/nicotine-plus/nicotine-plus/issues/1821)
 * When a filename is 255 characters long ([#1825](https://github.com/nicotine-plus/nicotine-plus/issues/1825))
 * Excessive memory usage when browsing large shares ([#1826](https://github.com/nicotine-plus/nicotine-plus/issues/1826))
 * Windows: Couldn't write to log file "/mu/.log" ([#1828](https://github.com/nicotine-plus/nicotine-plus/issues/1828))
 * Windows: "String too long" crash on notification popup ([#1829](https://github.com/nicotine-plus/nicotine-plus/issues/1829))
 * Windows: Spaces at the end of directories are trimmed when creating ([#1835](https://github.com/nicotine-plus/nicotine-plus/issues/1835))
 * Connect to remote host? ([#1839](https://github.com/nicotine-plus/nicotine-plus/issues/1839))
 * Error message appeard while trying to exit the client ([#1850](https://github.com/nicotine-plus/nicotine-plus/issues/1850))
 * \[3.2.1.rc2\] Crash when resuming transfers ([#1853](https://github.com/nicotine-plus/nicotine-plus/issues/1853))
 * Way to handle lots of small files on your upload queue ([#1865](https://github.com/nicotine-plus/nicotine-plus/issues/1865))


## Version 3.2.0 (December 18, 2021)

WINDOWS USERS: The installer format has changed in Nicotine+ 3.2.0 and above. If you are upgrading from Nicotine+ 3.1.1 or earlier, please uninstall Nicotine+ first (this will not remove your existing settings).

### Changes

 * Performance improvements across the entire application, including file searching, transfers, user shares and chats
 * Accessibility improvements to various components, including result filters, browse shares, wishlist and chat rooms
 * Several new keyboard shortcuts for easier navigation, a list of shortcuts can be viewed by pressing the F1 key
 * User interface improvements, including several clean-ups related to core client functions and preferences
 * Added an emoji picker in chat text entry
 * Added an option to disable search history
 * Increased the number of search history items from 15 to 200
 * Double-clicking a folder in search results now downloads the folder
 * Moved main tab visibility settings to "User Interface" category in preferences dialog
 * Moved log category options to right-click menu in log history pane
 * The 'When closing Nicotine+' preference now also applies when pressing Ctrl+Q
 * Improved terminology used for various client functions, including clearer output of the status bar and log history
 * Removed a few outdated and obsolete preferences
 * Removed the option to automatically share completed downloads, convert to standard shared folder
 * The Leech Detector plugin now sends the polite message after a leecher's first download has finished
 * New and improved translations for many languages
 * Lowered Python version requirement to 3.5 for Debian Stretch LTS based distros

### Corrections

 * Several stability improvements related to file scanning
 * Fixed issues where UPnP did not work with certain routers
 * Fixed an issue where the password could not be changed while logged out
 * Fixed an issue where inaccurate bitrates and durations were reported for certain files after scanning shares
 * Fixed a critical error when hiding the "Chat Rooms" tab
 * Fixed an issue where column header menus did not work in older GTK versions
 * Fixed an issue where column widths would not be remembered if multiple tabs were open
 * Fixed critical errors when quitting Nicotine+ in certain cases
 * Fixed a critical error when receiving invalid search results
 * Fixed an issue where uploads could not be manually resumed after a connection error
 * Fixed an issue where certain special characters were not removed from search terms
 * Fixed an issue where taskbar notifications were not cleared in older GTK versions
 * Fixed an issue where transfer statistics did not update properly
 * Fixed an issue where the tray icon did not appear in LXDE
 * Fixed an issue where tab notification highlights were removed too early
 * Fixed an issue where fetching data from Last.fm was unsuccessful in certain cases
 * Fixed an issue where the scrollbar could not be dragged from the edge of the window in the Breeze theme
 * Fixed an issue where the preferences dialog was too large on small screen resolutions
 * Network interface binding can now be used on systems with Linux <5.7 kernel
 * Debian: the stable PPA is compatible with Debian again
 * macOS: fixed an issue where the main window did not render in macOS Monterey
 * Windows: improved compatibility with Windows 11
 * Windows: reduced the number of false antivirus positives

### Issues closed on GitHub

 * It's possible to open more than one instance of Nicotine+ ([#1418](https://github.com/nicotine-plus/nicotine-plus/issues/1418))
 * Nicotine+ database needs recovery ([#1467](https://github.com/nicotine-plus/nicotine-plus/issues/1467))
 * Feature request: Option to not remember search history ([#1468](https://github.com/nicotine-plus/nicotine-plus/issues/1468))
 * Double-click on search result to start download ([#1469](https://github.com/nicotine-plus/nicotine-plus/issues/1469))
 * Consider bumping listen socket backlog length ([#1471](https://github.com/nicotine-plus/nicotine-plus/issues/1471))
 * Generate releases hashes? ([#1473](https://github.com/nicotine-plus/nicotine-plus/issues/1473))
 * Mac Intel El Capitan 10.11.6 ([#1474](https://github.com/nicotine-plus/nicotine-plus/issues/1474))
 * Raspbian support ([#1476](https://github.com/nicotine-plus/nicotine-plus/issues/1476))
 * The Nicotine+ project's title summary contains superfluous text about the function of the client ([#1481](https://github.com/nicotine-plus/nicotine-plus/issues/1481))
 * Catch-22 regarding password ([#1483](https://github.com/nicotine-plus/nicotine-plus/issues/1483))
 * Pressing Ctrl+? does not open the Keyboard Shortcuts window as expected ([#1484](https://github.com/nicotine-plus/nicotine-plus/issues/1484))
 * Tabs cannot be navigated without using mouse (accessibility) ([#1485](https://github.com/nicotine-plus/nicotine-plus/issues/1485))
 * It reads "(privileged)" in the size column of an upload transfer, but I've not privileged anybody, why? ([#1487](https://github.com/nicotine-plus/nicotine-plus/issues/1487))
 * Is Python version of >=3.6 really needed as a Build-Depends parameter? ([#1488](https://github.com/nicotine-plus/nicotine-plus/issues/1488))
 * Implement Ctrl-C text copying for selected elements in treeview ([#1490](https://github.com/nicotine-plus/nicotine-plus/issues/1490))
 * GtkTreeView column header context menus are out-of-context on MX Linux Continuum 18.3 ([#1492](https://github.com/nicotine-plus/nicotine-plus/issues/1492))
 * Search Scope button pop-up menu items positioned above top of screen (Linux) ([#1495](https://github.com/nicotine-plus/nicotine-plus/issues/1495))
 * Filter bar layout issues (Result Filters) ([#1497](https://github.com/nicotine-plus/nicotine-plus/issues/1497))
 * Text Entry should validate and execute upon input when focus moves away (Result Filters) ([#1498](https://github.com/nicotine-plus/nicotine-plus/issues/1498))
 * Text Entry should respond to a zero-length string created by any keypress event to force clear the filter (Result Filters) ([#1499](https://github.com/nicotine-plus/nicotine-plus/issues/1499))
 * Fix missing Alt+R accelerator for Result Filter bar show/hide button in Search Files ([#1500](https://github.com/nicotine-plus/nicotine-plus/issues/1500))
 * Redundant Find pop-up TextBox in Search Files TreeView widget hinders Ctrl+F so it needs to be disabled ([#1501](https://github.com/nicotine-plus/nicotine-plus/issues/1501))
 * Primary Tab Bar fails to surrender focus after second mouse-click (Main Window) ([#1502](https://github.com/nicotine-plus/nicotine-plus/issues/1502))
 * Put the options for Tab Label Colors into the Tab section (Preferences) ([#1505](https://github.com/nicotine-plus/nicotine-plus/issues/1505))
 * Scrap the redundant 'Clear All Colors' button from User Interface category (Preferences) ([#1506](https://github.com/nicotine-plus/nicotine-plus/issues/1506))
 * General captions of General sections generally conflict with General category name, in general (Preferences) ([#1507](https://github.com/nicotine-plus/nicotine-plus/issues/1507))
 * Dialog box drawn larger than small screen size makes OK and Apply buttons invisible (Preferences) ([#1508](https://github.com/nicotine-plus/nicotine-plus/issues/1508))
 * Remove Alt+F accelerator from Clear Finished button in Downloads and Uploads (Transfers) ([#1510](https://github.com/nicotine-plus/nicotine-plus/issues/1510))
 * Set default focus to the Username text entry box if there are no secondary tabs (User Browse, Info, Private Chat) ([#1511](https://github.com/nicotine-plus/nicotine-plus/issues/1511))
 * Chat view context-menu Copy has no function when nothing is selected (Chat) ([#1512](https://github.com/nicotine-plus/nicotine-plus/issues/1512))
 * Ctrl+F should open Find bar while chat text entry box has focus (Chat) ([#1513](https://github.com/nicotine-plus/nicotine-plus/issues/1513))
 * Alt+M for Send _Message conflicts with native _Mode menu in User Info ([#1515](https://github.com/nicotine-plus/nicotine-plus/issues/1515))
 * Alt+S for Free _Slot conflicts with native _Shares menu in Search Files (Filters) ([#1516](https://github.com/nicotine-plus/nicotine-plus/issues/1516))
 * Ability to scroll when you push the mouse to the rightmost edge of the screen (last pixel). ([#1517](https://github.com/nicotine-plus/nicotine-plus/issues/1517))
 * Swapping between gdbm/semidbm causes Serious [Errno 20] corrupted database error unhandled ([#1519](https://github.com/nicotine-plus/nicotine-plus/issues/1519))
 * Edit debug error string: "Shared files database index seems to be corrupted, rescan your shares" (add 'index') ([#1520](https://github.com/nicotine-plus/nicotine-plus/issues/1520))
 * Add entry to local debug log to identify Nicotine+ version and exact Python version being used at runtime ([#1521](https://github.com/nicotine-plus/nicotine-plus/issues/1521))
 * Show Similar Users button disappears off window edge due to widget alignment issues (Interests tab) ([#1523](https://github.com/nicotine-plus/nicotine-plus/issues/1523))
 * Nicotine crashes upon quitting ([#1525](https://github.com/nicotine-plus/nicotine-plus/issues/1525))
 * Plugin System Expansion ([#1542](https://github.com/nicotine-plus/nicotine-plus/issues/1542))
 * Notification badge cleared too early ([#1543](https://github.com/nicotine-plus/nicotine-plus/issues/1543))
 * Feature Request: Upload tab when someone uploads from you ([#1544](https://github.com/nicotine-plus/nicotine-plus/issues/1544))
 * Gtk 3 Bug: MacOS gtk_widget gdk_window ([#1545](https://github.com/nicotine-plus/nicotine-plus/issues/1545))
 * Search issue ([#1547](https://github.com/nicotine-plus/nicotine-plus/issues/1547))
 * Bug: 3.2.0 dev Arch Linux Error loading plugin libhunspell and libaspell ([#1548](https://github.com/nicotine-plus/nicotine-plus/issues/1548))
 * Arch Linux GTK 4.4.0 crashes upon quitting if double login ([#1552](https://github.com/nicotine-plus/nicotine-plus/issues/1552))
 * Arch Linux GTK 4.4.0 Allocation width too small needs at least 31x25 ([#1553](https://github.com/nicotine-plus/nicotine-plus/issues/1553))
 * Moving mouse over the dragging-point of a column/frame doesn't change the mouse pointer ([#1561](https://github.com/nicotine-plus/nicotine-plus/issues/1561))
 * \[3.2.0.dev1\] Always crash on leave Public room feed tab close (Chat Rooms) ([#1562](https://github.com/nicotine-plus/nicotine-plus/issues/1562))
 * Uploads with special characters in path cancelled ([#1564](https://github.com/nicotine-plus/nicotine-plus/issues/1564))
 * UPnP doesn't work ([#1566](https://github.com/nicotine-plus/nicotine-plus/issues/1566))
 * Crash Report on Windows 10: 'Box' object has no attribute 'add_action' ([#1569](https://github.com/nicotine-plus/nicotine-plus/issues/1569))
 * Critical Error that I'm getting after updating ([#1572](https://github.com/nicotine-plus/nicotine-plus/issues/1572))
 * Still Critical Error ([#1573](https://github.com/nicotine-plus/nicotine-plus/issues/1573))
 * lastfm: Could not get recent track from audioscrobbler ([#1574](https://github.com/nicotine-plus/nicotine-plus/issues/1574))
 * Critical error after closing search tab ([#1575](https://github.com/nicotine-plus/nicotine-plus/issues/1575))
 * UPnP stopped working with current unstable build ([#1580](https://github.com/nicotine-plus/nicotine-plus/issues/1580))
 * Trigger Browse Files once when online for Buddy List ([#1583](https://github.com/nicotine-plus/nicotine-plus/issues/1583))
 * Wishlist ([#1591](https://github.com/nicotine-plus/nicotine-plus/issues/1591))
 * Remove - hyphen ([#1592](https://github.com/nicotine-plus/nicotine-plus/issues/1592))
 * Failed to execute script nictoine win 10 ([#1597](https://github.com/nicotine-plus/nicotine-plus/issues/1597))
 * Wishlist quick search ([#1599](https://github.com/nicotine-plus/nicotine-plus/issues/1599))
 * Wishlist hot key ([#1600](https://github.com/nicotine-plus/nicotine-plus/issues/1600))
 * Filters button ([#1601](https://github.com/nicotine-plus/nicotine-plus/issues/1601))
 * Pressing enter in the wishlist when the line is empty ([#1603](https://github.com/nicotine-plus/nicotine-plus/issues/1603))
 * Keeps telling me my database is corrupt ([#1620](https://github.com/nicotine-plus/nicotine-plus/issues/1620))
 * I do not know if it's bug or not ([#1623](https://github.com/nicotine-plus/nicotine-plus/issues/1623))
 * Serious error occurred while rescanning shares ([#1625](https://github.com/nicotine-plus/nicotine-plus/issues/1625))
 * No idea, that's what I saw, when I came back ([#1626](https://github.com/nicotine-plus/nicotine-plus/issues/1626))
 * Wrong password results in lockdown ([#1627](https://github.com/nicotine-plus/nicotine-plus/issues/1627))
 * Cannot find gdbm or semidm on openbsd ([#1631](https://github.com/nicotine-plus/nicotine-plus/issues/1631))
 * Critical Error on Launch ([#1633](https://github.com/nicotine-plus/nicotine-plus/issues/1633))
 * Pop up about translated languages ([#1635](https://github.com/nicotine-plus/nicotine-plus/issues/1635))
 * Nicotine+ has encountered a critical error ([#1636](https://github.com/nicotine-plus/nicotine-plus/issues/1636))
 * Logs reporting 0 folders found after rescan ([#1642](https://github.com/nicotine-plus/nicotine-plus/issues/1642))
 * Crashed on expanding folder ([#1643](https://github.com/nicotine-plus/nicotine-plus/issues/1643))
 * Remove wish not possible when search contains parens ([#1652](https://github.com/nicotine-plus/nicotine-plus/issues/1652))
 * Critical Error ([#1654](https://github.com/nicotine-plus/nicotine-plus/issues/1654))
 * Leech Detector not working??!! ([#1656](https://github.com/nicotine-plus/nicotine-plus/issues/1656))
 * Nicotine+ not working with latest MacOS Monteray ([#1660](https://github.com/nicotine-plus/nicotine-plus/issues/1660))
 * \[3.2.0.dev1\] Critical error on popover context menu when disconnected ([#1662](https://github.com/nicotine-plus/nicotine-plus/issues/1662))
 * Nicotine Critical Error Operation not permitted ([#1663](https://github.com/nicotine-plus/nicotine-plus/issues/1663))
 * \[3.2.0.dev1\] Nicotine+ x64 fails to launch with "Failed to execute script nicotine" error ([#1665](https://github.com/nicotine-plus/nicotine-plus/issues/1665))
 * Nicotine+ has encountered a critical error ([#1666](https://github.com/nicotine-plus/nicotine-plus/issues/1666))
 * Critical Error "Value: 'Box' object has no attribute 'add_action'" ([#1670](https://github.com/nicotine-plus/nicotine-plus/issues/1670))
 * Bug with user status ([#1680](https://github.com/nicotine-plus/nicotine-plus/issues/1680))
 * Critical Error: Value: 'NoneType' object has no attribute 'get_hilite_image' ([#1682](https://github.com/nicotine-plus/nicotine-plus/issues/1682))
 * Having several issues getting all my files to share, or share correctly ([#1686](https://github.com/nicotine-plus/nicotine-plus/issues/1686))
 * Crash on Ctrl+W in Search tab ([#1692](https://github.com/nicotine-plus/nicotine-plus/issues/1692))
 * Move to Tray on Exit ([#1694](https://github.com/nicotine-plus/nicotine-plus/issues/1694))
 * OSError on Manjaro Linux ([#1703](https://github.com/nicotine-plus/nicotine-plus/issues/1703))
 * Conform to Windows window-arrangement hotkeys ([#1704](https://github.com/nicotine-plus/nicotine-plus/issues/1704))
 * Cannot Use App or See App Window (MacOS Monterey) ([#1709](https://github.com/nicotine-plus/nicotine-plus/issues/1709))
 * Crash report on "About Nicotine+" ([#1715](https://github.com/nicotine-plus/nicotine-plus/issues/1715))
 * 3.2.0.rc2 64-bit portable won't launch (Windows) ([#1724](https://github.com/nicotine-plus/nicotine-plus/issues/1724))
 * Clicking in a result filter field scrolls the results list to the top ([#1732](https://github.com/nicotine-plus/nicotine-plus/issues/1732))
 * Result filter fields cause results list to require an extra click ([#1733](https://github.com/nicotine-plus/nicotine-plus/issues/1733))
 * UI hangs for seconds at a time in the Search Files view ([#1734](https://github.com/nicotine-plus/nicotine-plus/issues/1734))
 * Scrolling on a Preferences field changes the field's value ([#1735](https://github.com/nicotine-plus/nicotine-plus/issues/1735))


## Version 3.1.1 (August 2, 2021)

### Changes

 * Downloads denied with 'Too many files' or 'Too many megabytes' are now re-queued every 12 minutes
 * Leech detector plugin opens private chat user tabs by default when sending complaints

### Corrections

 * IMPORTANT: Fixed an issue where recently queued files were uploaded before older files (LIFO queue behavior)
 * Fixed a crash when attempting to search files in joined rooms
 * Queue positions are now properly updated for queued uploads
 * Certain special characters needed to receive proper search results are no longer removed from search terms
 * Fixed an issue where decimals were truncated before being saved (e.g. in the 'Anti SHOUT' plugin)
 * Fixed an issue where an incorrect user tab was opened when issuing the /msg command

### Issues closed on GitHub

 * non US locale float type variables in plugins cannot be filled ([#1462](https://github.com/nicotine-plus/nicotine-plus/issues/1462))
 * Files uploaded in a random order ([#1463](https://github.com/nicotine-plus/nicotine-plus/issues/1463))


## Version 3.1.0 (July 23, 2021)

### Changes

 * Added alternative transfer speed limits for downloads and uploads, toggleable with a quick access button in the status bar
 * Added an option to save downloads to subfolders based on the uploader's username
 * Added a dropdown menu in file transfer views to clear various types of file transfers from the list
 * Added an option to disable reverse file paths in search results and file transfer views
 * Added an option to show private/locked search results and shared files from SoulseekQt clients
 * Added an option to only allow trusted buddies to access buddy shares
 * Added a context menu item in file transfer views to browse folders of file transfers, similar to search results
 * Added checkboxes to 'Shares' preferences to easily specify whether a shared folder should be buddy-only or not
 * Added a menu item to quickly toggle dark mode/theme, available under Menu -> View -> Prefer Dark Mode
 * Added debug logging categories for downloads, uploads and chats
 * Improved GUI accessibility for blind users using screen readers
 * Finished downloads are no longer cleared on disconnect/exit
 * Finished uploads are now restored on startup, unless previously cleared
 * Spam filter plugin now filters phrases in chat rooms in addition to private chats
 * Command aliases can now run chat commands, e.g. '/alias hello /away' will create a '/hello' command that runs '/away'
 * Unified preferences related to the GUI, such as colors, icons and tabs, under a single 'User Interface' page
 * A single preference now controls the maximum number of visible search results, instead of two separate preferences
 * Added a basic 'headless' mode to run Nicotine+ without a GUI, available through the --headless command line flag
 * Added the ability to start multiple instances of Nicotine+ when a custom config file is specified with the --config command line flag
 * Added the option to specify a custom user data folder location (used for storing e.g. the list of shared files) with the --user-data command line flag
 * Added plugin notifications for started/finished transfers
 * Various deprecations related to plugins, listed in pluginsystem.py and logged on startup
 * Various performance improvements
 * macOS: minor UX improvements to better align with macOS conventions
 * GNU/Linux and macOS: added an option to enforce a specific network interface, useful for virtual private networks (VPN)
 * Removed 'direct private message' toggle, since the official Soulseek clients do not understand such messages
 * Removed option to rotate tab labels, due to various issues with its implementation
 * Removed support for Ubuntu 16.04 and Python 3.5

### Corrections

 * Fixed an issue where file transfers did not reach maximum speeds on slow connections
 * Fixed an issue where incorrect upload speeds were sent to the server
 * Fixed an issue where failed downloads were marked as finished in cases where the download folder is not accessible
 * Fixed an issue where double-clicking treeview column headers activated the first row
 * Fixed an issue where the 'unread tabs' menu caused a crash if tabs were closed
 * Fixed an issue where adding finished downloads to shared files could result in a crash
 * Fixed an issue where searching a user's share could result in a crash after a refresh
 * Fixed a crash when attempting to show file properties for a user/folder row
 * Fixed various UPnP port forwarding issues with certain routers
 * Added a workaround for cases where Soulseek NS clients send incorrect file sizes for large files
 * Various GUI-related changes and improvements to reduce the number of inconsistencies
 * macOS: keyboard shortcuts now use the Command key instead of Ctrl
 * Windows: improvements to notifications to prevent duplicate tray icons
 * Windows: fixed an issue where closed windows would appear in window peek
 * Windows: fixed an issue where minimized windows were not displayed when restoring Nicotine+ from tray

### Issues closed on GitHub

 * Is there a way to exclude a file/directory from a share? + Some feedback ([#924](https://github.com/nicotine-plus/nicotine-plus/issues/924))
 * Feature Request: Improve folder folding behavior + Add Collapse/Expand All ([#981](https://github.com/nicotine-plus/nicotine-plus/issues/981))
 * Suggestion: Room wall improvements ([#985](https://github.com/nicotine-plus/nicotine-plus/issues/985))
 * Practical: change share from public to buddy and vice versa. ([#991](https://github.com/nicotine-plus/nicotine-plus/issues/991))
 * Version 3.0.1 and 3.0.2's Nicotine+.exe detected as a virus by Malwarebytes ([#1012](https://github.com/nicotine-plus/nicotine-plus/issues/1012))
 * Quicker access to speed throttling? ([#1031](https://github.com/nicotine-plus/nicotine-plus/issues/1031))
 * Copy/Paste keyboard shortcuts broken on Mac ([#1342](https://github.com/nicotine-plus/nicotine-plus/issues/1342))
 * Don't automatically clear downloads/uploads on quit ([#1343](https://github.com/nicotine-plus/nicotine-plus/issues/1343))
 * Notifications tray icons aren't removed automatically ([#1354](https://github.com/nicotine-plus/nicotine-plus/issues/1354))
 * Download to a \*username\* / subfolder ([#1355](https://github.com/nicotine-plus/nicotine-plus/issues/1355))
 * Drop official support for Ubuntu 16.04 ([#1360](https://github.com/nicotine-plus/nicotine-plus/issues/1360))
 * Headless support ([#1362](https://github.com/nicotine-plus/nicotine-plus/issues/1362))
 * Support for macOS High Sierra ([#1366](https://github.com/nicotine-plus/nicotine-plus/issues/1366))
 * Prevent Downloads from Displaying in the Debug Logging Window ([#1371](https://github.com/nicotine-plus/nicotine-plus/issues/1371))
 * Malware detection ([#1373](https://github.com/nicotine-plus/nicotine-plus/issues/1373))
 * Minimized window app won't show up when called from the system tray ([#1374](https://github.com/nicotine-plus/nicotine-plus/issues/1374))
 * Change close button position on macOS ([#1376](https://github.com/nicotine-plus/nicotine-plus/issues/1376))
 * Change menu action on macOS ([#1377](https://github.com/nicotine-plus/nicotine-plus/issues/1377))
 * Limit Buddy Shares to Trusted Buddies ([#1382](https://github.com/nicotine-plus/nicotine-plus/issues/1382))
 * Critical errors ([#1383](https://github.com/nicotine-plus/nicotine-plus/issues/1383))
 * Option to disable popup ([#1386](https://github.com/nicotine-plus/nicotine-plus/issues/1386))
 * Prevent notification balloon crashes on 32-bit Windows ([#1393](https://github.com/nicotine-plus/nicotine-plus/issues/1393))
 * ", line 127 ([#1395](https://github.com/nicotine-plus/nicotine-plus/issues/1395))
 * Auto-Size Columns Opens File in Player ([#1396](https://github.com/nicotine-plus/nicotine-plus/issues/1396))
 * Window Preview Shows Preferences Window ([#1397](https://github.com/nicotine-plus/nicotine-plus/issues/1397))
 * Crash report ([#1398](https://github.com/nicotine-plus/nicotine-plus/issues/1398))
 * Windows Defender / Trojan:Win32/Zpevdo.B ...False Positive? ([#1401](https://github.com/nicotine-plus/nicotine-plus/issues/1401))
 * Nicotine+ encountered a critical error and needs to exit ([#1402](https://github.com/nicotine-plus/nicotine-plus/issues/1402))
 * Middle-clicking user/share/room does not close it anymore ([#1404](https://github.com/nicotine-plus/nicotine-plus/issues/1404))
 * problem with access to some users. ([#1405](https://github.com/nicotine-plus/nicotine-plus/issues/1405))
 * Critical Error on master ([#1406](https://github.com/nicotine-plus/nicotine-plus/issues/1406))
 * Config error: can't decode 'searches' section 'group_searches' value ([#1407](https://github.com/nicotine-plus/nicotine-plus/issues/1407))
 * Transfer lists are cleared upon disconnection ([#1409](https://github.com/nicotine-plus/nicotine-plus/issues/1409))
 * Wishlists aren't being searched ([#1410](https://github.com/nicotine-plus/nicotine-plus/issues/1410))
 * Every downloaded file remains as "INCOMPLETE[number]Filename" ([#1411](https://github.com/nicotine-plus/nicotine-plus/issues/1411))
 * Exclamation point in the chat tab bar i have not seen before ([#1413](https://github.com/nicotine-plus/nicotine-plus/issues/1413))
 * Tried unpacking zip, scanner shows Gen:Variant.Bulz.495404 ([#1414](https://github.com/nicotine-plus/nicotine-plus/issues/1414))
 * Crash on getting File Properties at user or directory entry level in Download tab ([#1415](https://github.com/nicotine-plus/nicotine-plus/issues/1415))
 * in Download tab, the Queue Position column is empty ([#1416](https://github.com/nicotine-plus/nicotine-plus/issues/1416))
 * Windows Defender quarantined nicotine+ because of "Trojan:Win32/Zpevdo.B" ([#1417](https://github.com/nicotine-plus/nicotine-plus/issues/1417))
 * Tabs go out off the screen where there are many, they should use several lines instead. ([#1420](https://github.com/nicotine-plus/nicotine-plus/issues/1420))
 * Search main tab: wish tabs always extra. ([#1422](https://github.com/nicotine-plus/nicotine-plus/issues/1422))
 * Can't click anything when in fullscreen ([#1423](https://github.com/nicotine-plus/nicotine-plus/issues/1423))
 * 'GeoIP' object has no attribute 'get_all' ([#1426](https://github.com/nicotine-plus/nicotine-plus/issues/1426))
 * Finished Downloads Autoclearing ([#1427](https://github.com/nicotine-plus/nicotine-plus/issues/1427))
 * 'NetworkFrame' object has no attribute 'InterfaceRow' ([#1430](https://github.com/nicotine-plus/nicotine-plus/issues/1430))
 * Browse Folder via Downloads tab ([#1432](https://github.com/nicotine-plus/nicotine-plus/issues/1432))
 * Leech detector logs not showing up ([#1433](https://github.com/nicotine-plus/nicotine-plus/issues/1433))
 * Crash when adding to buddy list from User info tab ([#1434](https://github.com/nicotine-plus/nicotine-plus/issues/1434))
 * How to access option to close only window (keep sharing files)? ([#1435](https://github.com/nicotine-plus/nicotine-plus/issues/1435))
 * error ([#1436](https://github.com/nicotine-plus/nicotine-plus/issues/1436))
 * DownloadQueuedNotification on end of downloaded file ([#1438](https://github.com/nicotine-plus/nicotine-plus/issues/1438))
 * Shift + Mouse wheel a fall ([#1440](https://github.com/nicotine-plus/nicotine-plus/issues/1440))
 * Convert organization URL to lowercase ([#1441](https://github.com/nicotine-plus/nicotine-plus/issues/1441))
 * random crash? ([#1442](https://github.com/nicotine-plus/nicotine-plus/issues/1442))
 * Crash when closing private Chat tab ([#1445](https://github.com/nicotine-plus/nicotine-plus/issues/1445))
 * Critical error upon attempted chat ([#1446](https://github.com/nicotine-plus/nicotine-plus/issues/1446))
 * Incorrectly reported upload speed ([#1449](https://github.com/nicotine-plus/nicotine-plus/issues/1449))
 * UPnP does not work on this network (Windows) ([#1453](https://github.com/nicotine-plus/nicotine-plus/issues/1453))
 * select ValueError: too many file descriptors in select() (Windows) ([#1456](https://github.com/nicotine-plus/nicotine-plus/issues/1456))
 * UPnP not working ([#1457](https://github.com/nicotine-plus/nicotine-plus/issues/1457))


## Version 3.0.6 (May 1, 2021)

### Changes

 * The message sent to users attempting to access geo-blocked content can now be customized

### Corrections

 * Fixed a few critical errors related to uploads and file selections
 * Chat search commands and the /ctcpversion command now work properly
 * Fixed Python 3.5 compatibility
 * Windows: fixed an issue where duplicate notification icons would appear in the tray

### Issues closed on GitHub

 * Geoblock Options ([#1028](https://github.com/nicotine-plus/nicotine-plus/issues/1028))
 * Notifications tray icons aren't removed automatically ([#1354](https://github.com/nicotine-plus/nicotine-plus/issues/1354))
 * critical error ([#1356](https://github.com/nicotine-plus/nicotine-plus/issues/1356))
 * Frequent crashes in 3.0.5 ([#1357](https://github.com/nicotine-plus/nicotine-plus/issues/1357))
 * Unable to search chat room ([#1359](https://github.com/nicotine-plus/nicotine-plus/issues/1359))
 * Critical error ([#1361](https://github.com/nicotine-plus/nicotine-plus/issues/1361))


## Version 3.0.5 (April 24, 2021)

### Changes

 * Replaced previous country flag icons with clearer ones
 * Improved performance when selecting a large number of transfers
 * Queue positions and failed downloads are now checked every three minutes instead of every minute, to reduce stress on the uploading user
 * Performance improvements for long buddy lists
 * Added a dropdown menu button in tab bars for unread notifications

### Corrections

 * Custom media player and file manager commands no longer reset after a restart
 * Fixed an issue where scanning of shared files malfunctioned if the UI didn't load in time
 * Fixed a critical error when a new room was joined while country flags were disabled
 * Fixed a critical error when attempting to add wishlist items while disconnected from the server
 * Fixed a critical error when attempting to use the /rescan chat command
 * Fixed a rare case where Nicotine+ could crash on startup
 * 'Send to Player' for files downloaded to a custom folder no longer fails
 * Private room operators are once again able to add users to the room
 * When browsing your own shares, viewing recently shared downloads no longer requires a restart
 * Attempting to download files of disconnected users now displays the 'User logged off' status immediately
 * Column widths of the currently selected user browse tab are now saved
 * Unified chat completion behavior of chat rooms and private chats
 * UI customizations are once again applied to the preferences dialog
 * Corrected the behavior of 'Abort User's Uploads' button in the uploads view
 * Text-To-Speech messages no longer overlap each other
 * Minor behavioral corrections related to file transfers

### Issues closed on GitHub

 * Download Folder function doesn't work from search when uploader is offline ([#511](https://github.com/nicotine-plus/nicotine-plus/issues/511))
 * nicotine crash, ([#1040](https://github.com/nicotine-plus/nicotine-plus/issues/1040))
 * Crash on startup ([#1041](https://github.com/nicotine-plus/nicotine-plus/issues/1041))
 * Replace usage of Gtk.Menu with Gio.Menu ([#1045](https://github.com/nicotine-plus/nicotine-plus/issues/1045))
 * critical error when exit user browse tab ([#1192](https://github.com/nicotine-plus/nicotine-plus/issues/1192))
 * Version 3.0.4 flagged by Windows Defender ([#1329](https://github.com/nicotine-plus/nicotine-plus/issues/1329))
 * critical error crash ([#1333](https://github.com/nicotine-plus/nicotine-plus/issues/1333))
 * File Manager and Media Player events are buggy ([#1335](https://github.com/nicotine-plus/nicotine-plus/issues/1335))
 * Filtering on file type causes crash ([#1337](https://github.com/nicotine-plus/nicotine-plus/issues/1337))
 * The shared folders are not shared anymore ([#1338](https://github.com/nicotine-plus/nicotine-plus/issues/1338))
 * Pausing a download ([#1339](https://github.com/nicotine-plus/nicotine-plus/issues/1339))
 * copy search team Bug ([#1348](https://github.com/nicotine-plus/nicotine-plus/issues/1348))
 * Can't save files.db: [Errno 13] ([#1352](https://github.com/nicotine-plus/nicotine-plus/issues/1352))


## Version 3.0.4 (April 7, 2021)

### Corrections

 * Invalid file names no longer break scanning of shared folders
 * Configuration changes are now saved if Nicotine+ is terminated (SIGTERM)
 * Fixed a case where the upload status displayed 'User logged off' after the user reconnected
 * Action buttons in the file properties dialog now stick to the bottom as intended
 * Windows: Nicotine+ no longer crashes on startup when translations are used

### Issues closed on GitHub

 * Critical UnicodeDecodeError on startup: 'utf-8' codec can't decode byte 0x92 in position 12: invalid start byte ([#1038](https://github.com/nicotine-plus/nicotine-plus/issues/1038))
 * You have no privileges left. They are not necessary, but allow your downloads to be queued ahead of non-privileged users. [Question] ([#1039](https://github.com/nicotine-plus/nicotine-plus/issues/1039))
 * line 642 ([#1042](https://github.com/nicotine-plus/nicotine-plus/issues/1042))
 * 'utf-8' codec can't encode characters(surrogates not allowed) ([#1043](https://github.com/nicotine-plus/nicotine-plus/issues/1043))


## Version 3.0.3 (April 1, 2021)

### Changes

 * Refactored download queuing to use the same system as the official client
 * Improved reliability and performance of the upload queue
 * Added a popup that appears whenever a critial error occurs in the program

### Corrections

 * Nicotine+ now starts properly when invalid download filters are detected
 * The configuration file no longer resets when running out of disk space
 * Improved reliability of downloading folders containing special characters from certain clients
 * Keyboard shortcuts are now functional on non-Latin keyboard layouts
 * Upload bandwidth limits are no longer incorrectly applied when upload slots limits are enabled
 * Reaching a specified upload speed limit no longer interferes with max bandwidth/upload slot limits
 * Illegal file path characters are now replaced before downloading a file, to prevent issues with FAT/NTFS drives on Unix-based systems
 * Directly searching a user's files now functions properly
 * In predefined search filters, the state of the 'Free Slots' filter is now saved properly
 * If user browse/info tabs were closed, they no longer reopen when loading new information
 * Fixed a few behavioral issues related to chat notifications
 * Fixed issues related to incorrect user statuses being displayed in some cases
 * The correct status color is now displayed for usernames in past private chat messages
 * Leaving the public room is possible once again
 * Avoid unnecessary network traffic related to number of shared folders and files
 * Reduced memory usage on Windows and macOS

### Issues closed on GitHub

 * Version 3.0.1 and 3.0.2's Nicotine+.exe detected as a virus by Malwarebytes ([#1012](https://github.com/nicotine-plus/nicotine-plus/issues/1012))
 * Username Wrong Color in Chat ([#1013](https://github.com/nicotine-plus/nicotine-plus/issues/1013))
 * free slot setup ([#1014](https://github.com/nicotine-plus/nicotine-plus/issues/1014))
 * 'invalid operation on closed shelf' while rescaning shares ([#1016](https://github.com/nicotine-plus/nicotine-plus/issues/1016))
 * Complete file remains in Incomplete Downloads folder ([#1019](https://github.com/nicotine-plus/nicotine-plus/issues/1019))
 * User's shared file list cannot be saved to disk, due to a mismatch in the number of arguments on function call. ([#1024](https://github.com/nicotine-plus/nicotine-plus/issues/1024))
 * Deprecated messages related to privileges? ([#1025](https://github.com/nicotine-plus/nicotine-plus/issues/1025))
 * line 716 ([#1026](https://github.com/nicotine-plus/nicotine-plus/issues/1026))
 * line 707 ([#1029](https://github.com/nicotine-plus/nicotine-plus/issues/1029))
 * line 666, ([#1030](https://github.com/nicotine-plus/nicotine-plus/issues/1030))
 * Problems with new interface in 3.0 ([#1033](https://github.com/nicotine-plus/nicotine-plus/issues/1033))
 * line 642 ([#1037](https://github.com/nicotine-plus/nicotine-plus/issues/1037))


## Version 3.0.2 (March 1, 2021)

### Corrections

 * Fixed a regression where users could not be added to the buddy list
 * Fixed an issue where file extension info could appear incorrectly in the transfer list
 * Fixed an issue where root directories were not shared properly

### Issues closed on GitHub

 * Cannot Add Users to Buddy List ([#1011](https://github.com/nicotine-plus/nicotine-plus/issues/1011))


## Version 3.0.1 (February 26, 2021)

### Changes

 * Improved UI performance when loading many search results
 * Main menu can now be opened using the F10 key
 * The list of keyboard shortcuts can now be opened using Ctrl+?
 * Away status is now remembered between sessions

### Corrections

 * Fixed several issues causing the status of an upload to be stuck if the user logged out
 * Fixed a few chat room commands that did not work previously
 * Fixed an issue where country flags were missing for some users that rejoined a room
 * Several improvements and bug fixes to the plugin system
 * Flatpak: added support for MPRIS in the Now Playing-feature
 * Windows: fixed an issue where root directories could not be shared
 * macOS: fixed an issue where Nicotine+ would crash on startup on some systems

### Issues closed on GitHub

 * New installation in Big Sur. Doesn't scan shared folders. ([#899](https://github.com/nicotine-plus/nicotine-plus/issues/899))
 * Download speed after restart ([#918](https://github.com/nicotine-plus/nicotine-plus/issues/918))
 * Pluginsystem related issues, views and ideas [Updated] ([#990](https://github.com/nicotine-plus/nicotine-plus/issues/990))
 * [Windows] Certifi not installed ([#996](https://github.com/nicotine-plus/nicotine-plus/issues/996))
 * Enable CTCP-like private message responses (client version) Bool ([#998](https://github.com/nicotine-plus/nicotine-plus/issues/998))
 * Sharing a whole hard disk drive content doesn't work ([#999](https://github.com/nicotine-plus/nicotine-plus/issues/999))
 * CTCP_VERSION broke ([#1001](https://github.com/nicotine-plus/nicotine-plus/issues/1001))
 * v3.0 not starting on macos big sur 11.2.1 ([#1002](https://github.com/nicotine-plus/nicotine-plus/issues/1002))
 * Make opening of Window's file manager (File Explorer) more generic ([#1004](https://github.com/nicotine-plus/nicotine-plus/issues/1004))
 * missing python req in setup.py ([#1006](https://github.com/nicotine-plus/nicotine-plus/issues/1006))


## Version 3.0.0 (February 12, 2021)

### Changes

 * Introduced a new design utilizing header bars (to use the old design, uncheck Menu -> View -> Use Header Bar)
 * Improved UI responsiveness when scanning shares
 * Improved UI performance when multiple tabs are open
 * Added transfer statistics dialog
 * Added help window for keyboard shortcuts
 * Added an option to set a global font
 * Added support for text completion when typing in the search entry
 * Added a "Browse Folder" option for search results
 * Search results can now be filtered by file type
 * Added an option to clear search and filter history
 * Columns can now be reordered by dragging them to the desired location
 * Context menus for tabs now include an option to close all tabs
 * Added context menu items for viewing and deleting logs (chatrooms, private chat, log pane)
 * Added a keyboard shortcut to close tabs (Ctrl+W / Alt+F4)
 * Context menus can now be opened by long-pressing on a touch screen
 * Context menus can now be opened with the keyboard (Menu Key / Shift+F10)
 * The number of selected files is now visible in context menus
 * Added an option to copy the file path of a selected file using Ctrl+C
 * Added file properties dialog for user browse
 * Improved the default color scheme
 * Several other minor improvements

### Corrections

 * Fixed an issue where upload speed limits were not applied on startup
 * Fixed an issue where UPnP portforwarding did not succeed with certain routers
 * Fixed an issue where enabling the geographical paranoia option would prevent search results from being delivered to others
 * Fixed issues where certain uploads would be stuck in a "Cancelled" state
 * Fixed a Windows-specific issue where the config file did not always save
 * Fixed an macOS-specific issue where opening a folder did not work
 * Fixed an issue where custom commands registered in plugins did not work
 * Several other minor corrections

### Issues closed on GitHub

 * Nicotine will not login to server ([#904](https://github.com/nicotine-plus/nicotine-plus/issues/904))
 * File not shared ! ([#905](https://github.com/nicotine-plus/nicotine-plus/issues/905))
 * Backup of the slide position in the user browse tab ([#908](https://github.com/nicotine-plus/nicotine-plus/issues/908))
 * Save share list to disk => user tab ([#909](https://github.com/nicotine-plus/nicotine-plus/issues/909))
 * Double-clicking on shares ([#917](https://github.com/nicotine-plus/nicotine-plus/issues/917))
 * Fix viewing of shared files ([#919](https://github.com/nicotine-plus/nicotine-plus/issues/919))
 * WinError 3, "the system cannot find the path specified" ([#920](https://github.com/nicotine-plus/nicotine-plus/issues/920))
 * Replace usage of GtkComboBox with GtkComboBoxText ([#921](https://github.com/nicotine-plus/nicotine-plus/issues/921))
 * nicotine-plus.org certificate expired ([#922](https://github.com/nicotine-plus/nicotine-plus/issues/922))
 * Cyrillic characters don't display correctly in chat rooms (Unicode issue?) ([#925](https://github.com/nicotine-plus/nicotine-plus/issues/925))
 * Log windows scroll back to begin after any new entry. ([#926](https://github.com/nicotine-plus/nicotine-plus/issues/926))
 * Config resetting when quitting and opening again ([#934](https://github.com/nicotine-plus/nicotine-plus/issues/934))
 * nicotine.po ([#936](https://github.com/nicotine-plus/nicotine-plus/issues/936))
 * Bug: Browsing your own shares with "Share only to buddies" enabled isn't possible via User browse ([#940](https://github.com/nicotine-plus/nicotine-plus/issues/940))
 * Bug: Displayed shared files count in Chat rooms / User info inconsistent ([#941](https://github.com/nicotine-plus/nicotine-plus/issues/941))
 * Feature Request: Clear filters button ([#944](https://github.com/nicotine-plus/nicotine-plus/issues/944))
 * Feature Request: Allow regular expressions in Country field of Search Filters ([#946](https://github.com/nicotine-plus/nicotine-plus/issues/946))
 * Config Bug: WinError 32 + WinError 2: Can't rename config file, error & The system cannot find the file specified ([#949](https://github.com/nicotine-plus/nicotine-plus/issues/949))
 * Feature Request: Clear Search Result Filter History ([#950](https://github.com/nicotine-plus/nicotine-plus/issues/950))
 * Feature Request: A method to quit via Tray Icon ([#951](https://github.com/nicotine-plus/nicotine-plus/issues/951))
 * Windows Bug: Can't bring Nicotine+ to the foreground if one of its popup windows are open ([#953](https://github.com/nicotine-plus/nicotine-plus/issues/953))
 * Windows Bug: Preferences popup window is slow to open on occasion ([#954](https://github.com/nicotine-plus/nicotine-plus/issues/954))
 * Now Playing ([#957](https://github.com/nicotine-plus/nicotine-plus/issues/957))
 * Filtering by "10m" gives files >=10MiB, but filtering "10MiB" gives files >=9.54MiB ([#961](https://github.com/nicotine-plus/nicotine-plus/issues/961))
 * Setting Plugin /commands ([#962](https://github.com/nicotine-plus/nicotine-plus/issues/962))
 * Feature Request: Search Wishlist: Change "Select All" Button to "Clear All" ([#963](https://github.com/nicotine-plus/nicotine-plus/issues/963))
 * Feature Request: Indication that a search tab was opened automatically by the wishlist ([#964](https://github.com/nicotine-plus/nicotine-plus/issues/964))
 * Feature Request: Option to choose the search result filter's tab bar position ([#965](https://github.com/nicotine-plus/nicotine-plus/issues/965))
 * Bug: Clearing all active filters requires double-Enter for next filter attempt ([#966](https://github.com/nicotine-plus/nicotine-plus/issues/966))
 * MacOS 11.1 Open folder fails ([#970](https://github.com/nicotine-plus/nicotine-plus/issues/970))
 * MacOS 11.1, open folder opens the wrong directory ([#971](https://github.com/nicotine-plus/nicotine-plus/issues/971))
 * MacOS 11.1, wrong flag in buddy list ([#972](https://github.com/nicotine-plus/nicotine-plus/issues/972))
 * New bundled UPnP is not working ([#973](https://github.com/nicotine-plus/nicotine-plus/issues/973))
 * Replace GtkFileChooserButton with a custom button widget ([#975](https://github.com/nicotine-plus/nicotine-plus/issues/975))
 * Windows: Toggle show / minimize app on taskbar icon click ([#976](https://github.com/nicotine-plus/nicotine-plus/issues/976))
 * Feature Request: Enable tooltips for long strings that are cut off by another column ([#977](https://github.com/nicotine-plus/nicotine-plus/issues/977))
 * What is causing the log "Filtered out inexact or incorrect search result ... from user X"? ([#979](https://github.com/nicotine-plus/nicotine-plus/issues/979))
 * Bug: Private chat tabs closed/discarded without manually doing so ([#983](https://github.com/nicotine-plus/nicotine-plus/issues/983))
 * Bug: Unable to reliably close search tabs via middle mouse button click ([#984](https://github.com/nicotine-plus/nicotine-plus/issues/984))
 * Feature Request: Log Viewer / Context menu items to browse logs in system text editor ([#986](https://github.com/nicotine-plus/nicotine-plus/issues/986))
 * Failure to report buddy shares ([#988](https://github.com/nicotine-plus/nicotine-plus/issues/988))


## Version 2.2.2 (December 15, 2020)

### Changes

 * Fixed an issue where the list of queued downloads would not be restored on startup


## Version 2.2.1 (December 14, 2020)

Changes

 * Fixed an issue where the file scanner wouldn't scan a folder completely if a hidden subfolder was detected
 * Fixed an issue where invalid audio metadata in shared files could cause stability issues while running Nicotine+
 * Fixed a crash when trying to start Nicotine+ on a non-English Windows system
 * Fixed an issue where a "File not shared" status was sent when attempting to upload certain files
 * Geo block feature is functional again
 * Translations for the menu bar now show up in the UI again

Issues closed on GitHub

 * No icons in FreeBSD ([#889](https://github.com/nicotine-plus/nicotine-plus/issues/889))
 * GeoBlock Not Blocking ([#891](https://github.com/nicotine-plus/nicotine-plus/issues/891))
 * Nicotine v2.2.0 immediately crashes on startup on Windows 10 v19042.630 ([#893](https://github.com/nicotine-plus/nicotine-plus/issues/893))


## Version 2.2.0 (December 4, 2020)

### Changes

 * Modernized the default icon theme and several parts of the UI
 * Searching for file names containing special characters returns more search results than previously
 * Reduced the number of connectivity issues when transferring files from and to other users
 * Downloading folders recursively works properly again
 * Updated keyboard shortcuts, since the old ones conflicted with accelerator keys
 * Tray icons are properly detected in more cases
 * User browse and user info tabs now open immediately when requesting info for users
 * Show info message if user shares can't be loaded
 * Minor performance improvements when uploading a lot of files
 * Slightly improved startup times
 * Improved UI responsiveness when browsing your own shares
 * Added option to minimize Nicotine+ to tray on startup
 * Added "Now Playing Search" plugin for searching files based on data from songs playing in your media player
 * Added "Now Playing Sender" plugin for automatically sending names of songs playing to select chat rooms
 * Builtin plugins load properly on Windows again
 * Modified config backup behavior to not back up the config if "Cancel" is pressed in the file chooser
 * Shares lists saved in older versions of Nicotine+ can now be loaded again
 * Peer-to-peer (direct) private messaging works properly again
 * Fixed a crash when checking for stuck downloads (regression in Nicotine+ 2.1.2)
 * General usability improvements to macOS builds
 * Removed option to stop responding to search requests for certain time periods
 * Removed dbus-python, libnotify, miniupnpc, pytaglib and xdg-utils dependencies, as functionality is now handled by Nicotine+
 * Multiple under-the-hood code improvements and code style changes, as well as smaller bug fixes

### Issues closed on GitHub

 * Brew OSX Install ([#58](https://github.com/nicotine-plus/nicotine-plus/issues/58))
 * a separate program for database scanning ([#443](https://github.com/nicotine-plus/nicotine-plus/issues/443))
 * Failed to map the external WAN port: Invalid Args ([#597](https://github.com/nicotine-plus/nicotine-plus/issues/597))
 * After requesting user info put that user's info tab on top. ([#651](https://github.com/nicotine-plus/nicotine-plus/issues/651))
 * Feature request: share and/or cache message connections to remote clients ([#663](https://github.com/nicotine-plus/nicotine-plus/issues/663))
 * Search Now playing ([#664](https://github.com/nicotine-plus/nicotine-plus/issues/664))
 * Compile pytaglib for Python 2 or 3? - Error Trying To Run 2.1.1 ([#726](https://github.com/nicotine-plus/nicotine-plus/issues/726))
 * Follow X Session Management Protocol ([#729](https://github.com/nicotine-plus/nicotine-plus/issues/729))
 * sometimes, nicotine eats all memory ([#750](https://github.com/nicotine-plus/nicotine-plus/issues/750))
 * provided extensions doesn't load ([#761](https://github.com/nicotine-plus/nicotine-plus/issues/761))
 * Enabled plugins are no more activated at startup ([#762](https://github.com/nicotine-plus/nicotine-plus/issues/762))
 * Plugin properties aren't editable ([#763](https://github.com/nicotine-plus/nicotine-plus/issues/763))
 * some users aren't browsable ([#766](https://github.com/nicotine-plus/nicotine-plus/issues/766))
 * tray icon problem ([#767](https://github.com/nicotine-plus/nicotine-plus/issues/767))
 * Connection issue ([#768](https://github.com/nicotine-plus/nicotine-plus/issues/768))
 * Uploads Cancelled ([#784](https://github.com/nicotine-plus/nicotine-plus/issues/784))
 * Download recursive ([#790](https://github.com/nicotine-plus/nicotine-plus/issues/790))
 * not sure if this is a bug or something else ([#791](https://github.com/nicotine-plus/nicotine-plus/issues/791))
 * Can't scan any songs ([#798](https://github.com/nicotine-plus/nicotine-plus/issues/798))
 * Search problem? ([#822](https://github.com/nicotine-plus/nicotine-plus/issues/822))
 * windows unstable build can't rebuild shares ([#829](https://github.com/nicotine-plus/nicotine-plus/issues/829))
 * Nicotine 2.1.2 fails to launch in FreeBSD due to missing pytaglib ([#843](https://github.com/nicotine-plus/nicotine-plus/issues/843))
 * Download Recursive ([#844](https://github.com/nicotine-plus/nicotine-plus/issues/844))
 * Option to start application hidden when tray icon enabled ([#864](https://github.com/nicotine-plus/nicotine-plus/issues/864))
 * Missing application icon from window list ([#879](https://github.com/nicotine-plus/nicotine-plus/issues/879))
 * Python 3.8 Crashes ([#882](https://github.com/nicotine-plus/nicotine-plus/issues/882))


## Version 2.1.2 (October 12, 2020)

### Changes

 * Contents of a shared folder are now properly sent to other users
 * Improved performance and memory usage when scanning shares
 * Large memory usage reductions when many rooms and private chats are open
 * Sharing downloaded files now works properly
 * Private messages sent while the user was offline are shown separately from new messages
 * Added transfer speeds and shortcuts to downloads/uploads in the tray
 * Multiple under-the-hood code improvements and code style changes

### Issues closed on GitHub

 * Improve code style/consistency ([#377](https://github.com/nicotine-plus/nicotine-plus/issues/377))
 * debian packages ([#530](https://github.com/nicotine-plus/nicotine-plus/issues/530))
 * running from source - missing reqs ([#531](https://github.com/nicotine-plus/nicotine-plus/issues/531))
 * SIGABRT when scanning corrupt/empty FLAC file ([#730](https://github.com/nicotine-plus/nicotine-plus/issues/730))


## Version 2.1.1 (September 26, 2020)

### Changes

 * Improved speed limit calculations for file transfers
 * Added option to enable dark mode theme
 * Added option to copy a previous search term when right-clicking a search tab
 * Replaced text search dialog with search bar
 * If multiple file transfers are in progress, the UI now updates properly
 * Auto-joining the public chat room now works properly
 * Copying text with Ctrl-C now works properly again
 * Added option to log debug messages to file
 * Several minor bug fixes

### Issues closed on GitHub

 * Please put whole search string after/before "results: x/y" ([#383](https://github.com/nicotine-plus/nicotine-plus/issues/383))
 * replace log search function with search/filter thingybob, send logs to logfile. ([#387](https://github.com/nicotine-plus/nicotine-plus/issues/387))
 * Transfer connection initiation following an unallowed (queued) transfer response ([#653](https://github.com/nicotine-plus/nicotine-plus/issues/653))
 * Minor issues to fix for 2.1.1 ([#659](https://github.com/nicotine-plus/nicotine-plus/issues/659))
 * Windows 10 dark theme support ([#661](https://github.com/nicotine-plus/nicotine-plus/issues/661))
 * Wrap filters into one line ([#669](https://github.com/nicotine-plus/nicotine-plus/issues/669))
 * Public room cannot be auto-joined ([#672](https://github.com/nicotine-plus/nicotine-plus/issues/672))


## Version 2.1.0 (September 12, 2020)

### Changes

 * Major performance improvements when rescanning shared files and sending user browse responses to others
 * Several performance and stability improvements related to connections and file transfers
 * Several Windows fixes regarding memory leaks, unresponsiveness and issues when starting Nicotine+
 * Reduced memory usage while rescanning shared files
 * Consistent startup times no matter the number of shared files.
   On large file shares, this cuts down startup times from tens of seconds to 1-2 seconds, depending on your hardware.
 * Numbers are now appended to the file names of duplicate downloads
 * Your personal upload speed is no longer reported as 0 B/s
 * In folder/user grouping mode, selecting a user or folder now allows you to retry/cancel all downloads under them
 * Added quick-access checkbox for enabling/disabling private room invitations
 * Replaced ticker banner with room wall, which displays individual messages from room users
 * "Send to player"-feature is functional again
 * Queue position of downloads is now asked automatically
 * The wishlist feature now works as intended, sending one search at a time instead of three. Wishlist items can also be renamed.
 * Improved notification settings
 * Improved readability in search results and transfer views
 * Several other UI fixes and improvements
 * A rare issue where all tabs were hidden on startup has been fixed
 * Using non-Latin characters in the Windows client now works properly again
 * The Windows installer size was reduced from ~40 MB to ~25 MB
 * The Windows installer now removes old Nicotine+ system files before updating installations
 * Removed support for detachable tabs due to low usage and bugs
 * Replaced Mutagen with pytaglib for audio file metadata scanning due to performance issues

### Issues closed on GitHub

 * Brew OSX Install ([#58](https://github.com/nicotine-plus/nicotine-plus/issues/58))
 * Flatpak build ([#102](https://github.com/nicotine-plus/nicotine-plus/issues/102))
 * Fix remaining GTK warnings ([#290](https://github.com/nicotine-plus/nicotine-plus/issues/290))
 * right click user implicitly selects all files downloading from that user. ([#308](https://github.com/nicotine-plus/nicotine-plus/issues/308))
 * two cds saved in the same folder ([#313](https://github.com/nicotine-plus/nicotine-plus/issues/313))
 * Fatal error detected" when trying to run Nicotine on Windows 10 ([#413](https://github.com/nicotine-plus/nicotine-plus/issues/413))
 * RAM usage ([#416](https://github.com/nicotine-plus/nicotine-plus/issues/416))
 * if no close button on tabs it's not possible to close User search file notebook ([#428](https://github.com/nicotine-plus/nicotine-plus/issues/428))
 * Question; what diff between scanning and rebuilding share ? ([#430](https://github.com/nicotine-plus/nicotine-plus/issues/430))
 * notify sharelist is empty ([#434](https://github.com/nicotine-plus/nicotine-plus/issues/434))
 * double click is received on selection despite being performed on blank space ([#437](https://github.com/nicotine-plus/nicotine-plus/issues/437))
 * align columns text to left, right or center ([#438](https://github.com/nicotine-plus/nicotine-plus/issues/438))
 * url catching stop to work since update of 2 days ago ([#457](https://github.com/nicotine-plus/nicotine-plus/issues/457))
 * Font worrie > ([#458](https://github.com/nicotine-plus/nicotine-plus/issues/458))
 * progress bar stuck at 100% ([#454](https://github.com/nicotine-plus/nicotine-plus/issues/454))
 * Question : how to auto-join a room ? ([#464](https://github.com/nicotine-plus/nicotine-plus/issues/464))
 * Every you can right click a user, but not in the chat, there it's left click. ([#466](https://github.com/nicotine-plus/nicotine-plus/issues/466))
 * Tree view expand/collapse is not respected on new transfer ([#473](https://github.com/nicotine-plus/nicotine-plus/issues/473))
 * application content is not displayed properly with tabs set to side ([#474](https://github.com/nicotine-plus/nicotine-plus/issues/474))
 * Completed downloads are re-Queued ([#477](https://github.com/nicotine-plus/nicotine-plus/issues/477))
 * search tab "close thistab" missing if 3 tabs are open ([#481](https://github.com/nicotine-plus/nicotine-plus/issues/481))
 * close button in About Nicotine+ doesn't work ([#485](https://github.com/nicotine-plus/nicotine-plus/issues/485))
 * Wishlist has issues with chinese characters ([#498](https://github.com/nicotine-plus/nicotine-plus/issues/498))
 * Wishlist - Ability to rename wishlist searches ([#499](https://github.com/nicotine-plus/nicotine-plus/issues/499))
 * Certain searches don't stop even after closing the tab, restarting the program, and/or disconnecting and reconnecting to Soulseek ([#520](https://github.com/nicotine-plus/nicotine-plus/issues/520))
 * stacktrace: struct.error: required argument is not an integer ([#527](https://github.com/nicotine-plus/nicotine-plus/issues/527))
 * something goes wrong .... ([#529](https://github.com/nicotine-plus/nicotine-plus/issues/529))
 * Warning: unknown object type 'bool' in message 'pynicotine.slskmessages.FileSearchResult' ([#535](https://github.com/nicotine-plus/nicotine-plus/issues/535))
 * regression on open files on OpenBSD ([#536](https://github.com/nicotine-plus/nicotine-plus/issues/536))
 * Chat messages went nowhere and I got this trace. ([#545](https://github.com/nicotine-plus/nicotine-plus/issues/545))
 * filter out unspecific searches ([#551](https://github.com/nicotine-plus/nicotine-plus/issues/551))
 * Mouse cursor does not indicate draggable borders ([#552](https://github.com/nicotine-plus/nicotine-plus/issues/552))
 * Network share issue ([#559](https://github.com/nicotine-plus/nicotine-plus/issues/559))
 * possibly worrie with upload stuck in connecting state if folder uploaded ([#564](https://github.com/nicotine-plus/nicotine-plus/issues/564))
 * Let user choose for International flag ([#569](https://github.com/nicotine-plus/nicotine-plus/issues/569))
 * Search -> Right Click -> Download folder(s) does nothing ([#574](https://github.com/nicotine-plus/nicotine-plus/issues/574))
 * Some weird characters prevents download of file ([#578](https://github.com/nicotine-plus/nicotine-plus/issues/578))
 * some margin lines are missing (possible qt/gtk issue) ([#593](https://github.com/nicotine-plus/nicotine-plus/issues/593))
 * arrows are missing from the tree view collapse/expand ([#594](https://github.com/nicotine-plus/nicotine-plus/issues/594))
 * Nicotine Freezes With Too Many Transfers ([#609](https://github.com/nicotine-plus/nicotine-plus/issues/609))


## Version 2.0.1 (July 16, 2020)

### Changes

 * Fixed an issue where search requests from others weren't processed
 * The update checker now shows the latest version properly


## Version 2.0.0 (July 14, 2020)

### Changes

 * Ported from Python 2 to Python 3
 * Ported from GTK2 to GTK3 (PyGTK to PyGObject)
 * Support for HiDPI displays
 * Search results and transfers can now be grouped by folder
 * Support for transfers larger than 2 GB in size
 * Transfers and search results now support drag-select
 * Performance improvements in downloads, uploads and search views
 * Special characters (e.g. -, ') are now removed from search terms by default, to receive more search results.
   This behavior can be toggled in Settings -> Misc -> Searches.
 * Excluding search results by placing a - sign in front of a word now works properly
 * Search filters now check the directory path
 * Column widths are now remembered between sessions
 * Added option to open previous tab on startup
 * Added option to hide buddy list
 * Custom messages can now be sent to leechers in Settings -> Misc -> Plugins -> Leech detector
 * Plugins are now bundled with Nicotine+ installations by default
 * Nicotine+ now follows the XDG Base Directory Specification
 * Replaced deprecated dependencies with maintained ones
 * Added unit and DEP-8 continuous integration testing
 * Minor UI cleanups
 * General code cleanups, removed dead code
 * Replaced non-free sound effects

### Issues closed on GitHub

 * Columns Position Not Being Maintained ([#8](https://github.com/nicotine-plus/nicotine-plus/issues/8))
 * Add "Group by folder" option to search results ([#17](https://github.com/nicotine-plus/nicotine-plus/issues/17))
 * Downloads tab hanging when adding a lot of files ([#34](https://github.com/nicotine-plus/nicotine-plus/issues/34))
 * NTFS support on linux ([#49](https://github.com/nicotine-plus/nicotine-plus/issues/49))
 * Show network drives when adding a shared directory. ([#52](https://github.com/nicotine-plus/nicotine-plus/issues/52))
 * send to player does not work. ([#53](https://github.com/nicotine-plus/nicotine-plus/issues/53))
 * CPU usage spikes and remains high after period of usage ([#54](https://github.com/nicotine-plus/nicotine-plus/issues/54))
 * Segfault When Getting User Info ([#57](https://github.com/nicotine-plus/nicotine-plus/issues/57))
 * Segmentation fault on Ubuntu Gnome 17.04 ([#60](https://github.com/nicotine-plus/nicotine-plus/issues/60))
 * filenames with ? in them get stuck on uploads list ([#61](https://github.com/nicotine-plus/nicotine-plus/issues/61))
 * Nicotine+ Windows 8.1 (64-bit) mutagen attempts to handle non-video files ([#62](https://github.com/nicotine-plus/nicotine-plus/issues/62))
 * Nicotine+ 1.4.1, windows 8.1 (64-bit) errors when using UPNP ([#63](https://github.com/nicotine-plus/nicotine-plus/issues/63))
 * Nicotine+ 1.4.1, windows 8.1 (64-bit) Spurious error messages ([#64](https://github.com/nicotine-plus/nicotine-plus/issues/64))
 * Nicotine + 1.4.1, windows 8.1 (64-bit) buttons not working ([#65](https://github.com/nicotine-plus/nicotine-plus/issues/65))
 * Downloads directory is not shared ([#66](https://github.com/nicotine-plus/nicotine-plus/issues/66))
 * Can't share directories ([#68](https://github.com/nicotine-plus/nicotine-plus/issues/68))
 * Question: Is Development Dead? ([#73](https://github.com/nicotine-plus/nicotine-plus/issues/73))
 * select ValueError: filedescriptor out of range in select() ([#77](https://github.com/nicotine-plus/nicotine-plus/issues/77))
 * blurry tray icon in kde plasma ([#81](https://github.com/nicotine-plus/nicotine-plus/issues/81))
 * Problems sharing files ([#83](https://github.com/nicotine-plus/nicotine-plus/issues/83))
 * Choosing "Download containing folder(s)" from search results does nothing ([#84](https://github.com/nicotine-plus/nicotine-plus/issues/84))
 * Uploads not working ([#85](https://github.com/nicotine-plus/nicotine-plus/issues/85))
 * UI very condensed on high-dpi linux. ([#88](https://github.com/nicotine-plus/nicotine-plus/issues/88))
 * Wishlist returns empty results for foreign characters ([#89](https://github.com/nicotine-plus/nicotine-plus/issues/89))
 * New Commits - Is Development Back? ([#90](https://github.com/nicotine-plus/nicotine-plus/issues/90))
 * Filter doesn't include directory path ([#91](https://github.com/nicotine-plus/nicotine-plus/issues/91))
 * XDG Base Directory Support ([#94](https://github.com/nicotine-plus/nicotine-plus/issues/94))
 * Port to python3 ([#99](https://github.com/nicotine-plus/nicotine-plus/issues/99))
 * Nicotine+ 1.4.2, Debian 9 (64-bit) Downloading file size >2GB appears as negative numbers, files near 4GB download 0 byte. ([#100](https://github.com/nicotine-plus/nicotine-plus/issues/100))
 * Nicotine+ 1.4.1 don't handle invalid characters in Windows ([#101](https://github.com/nicotine-plus/nicotine-plus/issues/101))
 * Random crash on Raspbian ([#103](https://github.com/nicotine-plus/nicotine-plus/issues/103))
 * Bitrate not shown for most music in search results ([#104](https://github.com/nicotine-plus/nicotine-plus/issues/104))
 * Nicotine+ 1.4.2, Debian 9 (64 bit) : Can't get shared files + current downloads disappeared : since the last but one update, from branch master ([#107](https://github.com/nicotine-plus/nicotine-plus/issues/107))
 * Website is badly out of date ([#109](https://github.com/nicotine-plus/nicotine-plus/issues/109))
 * images seem to be integrated from the launch directory if they have special names ([#113](https://github.com/nicotine-plus/nicotine-plus/issues/113))
 * Not working on Ubuntu 20.04 Focal Fossa ([#115](https://github.com/nicotine-plus/nicotine-plus/issues/115))
 * Please update Nicotine to work on the latest Ubuntu (20.04) ([#123](https://github.com/nicotine-plus/nicotine-plus/issues/123))
 * Compiled 'Master Branch' - Nicotine is Black Blank Screen? ([#140](https://github.com/nicotine-plus/nicotine-plus/issues/140))
 * Question: 1.4.3 - Columns Hiding? ([#143](https://github.com/nicotine-plus/nicotine-plus/issues/143))
 * info user correct extra typo ([#144](https://github.com/nicotine-plus/nicotine-plus/issues/144))
 * select user transfer does not select anything ([#145](https://github.com/nicotine-plus/nicotine-plus/issues/145))
 * clicking hyperlinks does not open browser ([#146](https://github.com/nicotine-plus/nicotine-plus/issues/146))
 * left click does not work on users nickname in rooms ([#147](https://github.com/nicotine-plus/nicotine-plus/issues/147))
 * Interest tab : text zone too small ([#148](https://github.com/nicotine-plus/nicotine-plus/issues/148))
 * request : adding file chooser preview widget in info user picture setting ([#149](https://github.com/nicotine-plus/nicotine-plus/issues/149))
 * menu separator does not follow gtk+ rules ([#151](https://github.com/nicotine-plus/nicotine-plus/issues/151))
 * 1.4.3 Linux - Hiding Tabs - Always Opens Now Under Buddy List ([#154](https://github.com/nicotine-plus/nicotine-plus/issues/154))
 * strace shows weird file access syscalls ([#155](https://github.com/nicotine-plus/nicotine-plus/issues/155))
 * (world) flags missing at startup / and buddy list ([#161](https://github.com/nicotine-plus/nicotine-plus/issues/161))
 * setup.py: DistutilsFileError ([#164](https://github.com/nicotine-plus/nicotine-plus/issues/164))
 * warnings causes by userlist resizing columns ([#165](https://github.com/nicotine-plus/nicotine-plus/issues/165))
 * Question: No more charsets selection ? ([#180](https://github.com/nicotine-plus/nicotine-plus/issues/180))
 * my gtk3 theme gives checkbuttons looks bigger ([#181](https://github.com/nicotine-plus/nicotine-plus/issues/181))
 * Question - Bug? - Log Window Issue ([#186](https://github.com/nicotine-plus/nicotine-plus/issues/186))
 * wait a minute, only spellchecker is missing ? ([#190](https://github.com/nicotine-plus/nicotine-plus/issues/190))
 * userlist for myself does not display files number ([#192](https://github.com/nicotine-plus/nicotine-plus/issues/192))
 * AttributeError in changecolour(): PrivateChat object has no attribute 'tag_log' ([#194](https://github.com/nicotine-plus/nicotine-plus/issues/194))
 * Add support for >2GB downloads ([#201](https://github.com/nicotine-plus/nicotine-plus/issues/201))
 * IndexError at start on Debian Buster ([#202](https://github.com/nicotine-plus/nicotine-plus/issues/202))
 * Speed up program startup times ([#215](https://github.com/nicotine-plus/nicotine-plus/issues/215))
 * custom tray icons not respected ([#239](https://github.com/nicotine-plus/nicotine-plus/issues/239))
 * Request: Modes Tab Placement? ([#242](https://github.com/nicotine-plus/nicotine-plus/issues/242))
 * text in log aera in chat rooms lag to display from entry ([#253](https://github.com/nicotine-plus/nicotine-plus/issues/253))
 * /now playing does not work after nic+ restart ([#255](https://github.com/nicotine-plus/nicotine-plus/issues/255))
 * add grouping by path ([#269](https://github.com/nicotine-plus/nicotine-plus/issues/269))
 * on kde LMB on tray icon brings menu, not app ([#270](https://github.com/nicotine-plus/nicotine-plus/issues/270))
 * lower on an int? ([#278](https://github.com/nicotine-plus/nicotine-plus/issues/278))
 * right-clicking file that user 2 downloads points to user 1 ([#297](https://github.com/nicotine-plus/nicotine-plus/issues/297))
 * Private Chat tab does not get notified on receiving a message ([#299](https://github.com/nicotine-plus/nicotine-plus/issues/299))
 * RMB doesn't select what's underneath it ([#300](https://github.com/nicotine-plus/nicotine-plus/issues/300))
 * unable to download to created folder ([#301](https://github.com/nicotine-plus/nicotine-plus/issues/301))
 * status never reach 100% because of filtered files ([#302](https://github.com/nicotine-plus/nicotine-plus/issues/302))
 * twice downloaded same folder, aborted duplicate files, remove aborted does not remove ([#305](https://github.com/nicotine-plus/nicotine-plus/issues/305))
 * downloading folder from user browse doesn't work ([#311](https://github.com/nicotine-plus/nicotine-plus/issues/311))
 * cannot connect ([#312](https://github.com/nicotine-plus/nicotine-plus/issues/312))
 * In download page, pressing Delete key removes 2 files instead of 1 ([#314](https://github.com/nicotine-plus/nicotine-plus/issues/314))
 * invalid path ([#318](https://github.com/nicotine-plus/nicotine-plus/issues/318))
 * Distrib message type 93 unknown ([#322](https://github.com/nicotine-plus/nicotine-plus/issues/322))
 * Connection issues after search ([#329](https://github.com/nicotine-plus/nicotine-plus/issues/329))
 * Window decorator close button doesn't work ([#330](https://github.com/nicotine-plus/nicotine-plus/issues/330))
 * Question: group by folders vs group by users ([#335](https://github.com/nicotine-plus/nicotine-plus/issues/335))
 * [#312](https://github.com/nicotine-plus/nicotine-plus/issues/312) continued, cannot connect ([#336](https://github.com/nicotine-plus/nicotine-plus/issues/336))
 * Can't find anything from Wu-tang ([#343](https://github.com/nicotine-plus/nicotine-plus/issues/343))
 * download stuck in a weird way ([#344](https://github.com/nicotine-plus/nicotine-plus/issues/344))
 * Peer messages causing socket error ([#346](https://github.com/nicotine-plus/nicotine-plus/issues/346))
 * expand/collapse all missing in upload tab ([#354](https://github.com/nicotine-plus/nicotine-plus/issues/354))
 * AttributeError: 'Uploads' object has no attribute 'transfers' ([#360](https://github.com/nicotine-plus/nicotine-plus/issues/360))
 * remove filtered files when autoremoving ([#374](https://github.com/nicotine-plus/nicotine-plus/issues/374))
 * wishlist searches should notify on finding a result, not on attempting to find something ([#380](https://github.com/nicotine-plus/nicotine-plus/issues/380))
 * Search log window case insensitive. ([#384](https://github.com/nicotine-plus/nicotine-plus/issues/384))
 * Gentoo upnp errors, failed to map the external wan port. ([#385](https://github.com/nicotine-plus/nicotine-plus/issues/385))


## Version 1.4.3 Unstable

* Rolling development release in preparation for 2.0.0


## Version 1.4.2 (February 17, 2018)

### Issues closed on GitHub

 * Bitrate - Length - Speed ([#45](https://github.com/nicotine-plus/nicotine-plus/issues/45))
 * bug or feature ? ([#47](https://github.com/nicotine-plus/nicotine-plus/issues/47))


## Version 1.4.1 (February 12, 2017)

### Issues closed on GitHub

 * 1.4.0 /usr/bin empty ([#38](https://github.com/nicotine-plus/nicotine-plus/issues/38))
 * Configure - Directories Page 4 of 5 ([#39](https://github.com/nicotine-plus/nicotine-plus/issues/39))
 * Configure - Username ([#40](https://github.com/nicotine-plus/nicotine-plus/issues/40))
 * 1.4.0 Text Off Set Under Columns ([#41](https://github.com/nicotine-plus/nicotine-plus/issues/41))
 * Make nicotine work with FreeBSD (PR [#44](https://github.com/nicotine-plus/nicotine-plus/issues/44))


## Version 1.4.0 (January 31, 2017)

### Miscellaneous bugs fixed

 * Some files were not shown in shares due to broken metadata of these files.
 * Fix a bug preventing the offline help to open.

### Features

 * Windows installer refreshed.

### Issues closed on GitHub

 * Make proper release ([#26](https://github.com/nicotine-plus/nicotine-plus/issues/26))

### Issues closed on Trac

 * File Manager / "Open Directory" function in Windows (#717)
 * Open Directory not working (#945)


## Version 1.3.2 Unstable (January 14, 2017)

### Issues closed on GitHub

 * Uploads stop working after a while ([#35](https://github.com/nicotine-plus/nicotine-plus/issues/35))
 * Can't download from certain users ([#37](https://github.com/nicotine-plus/nicotine-plus/issues/37))

### Issues closed on Trac

 * shared files appear not shared to some peers (#744)
 * Stops Downloading After About 15 Minutes (#759)
 * Browse Files from Friemds (#762)
 * Download issue.... (#903)


## Version 1.3.1 Unstable (January 10, 2017)

### Behavior

 * Displaying results of searches should now be faster and not blocking the UI.
 * Send a private message to users who queue a directory has been removed.
 * Hidden directories on Windows are not shared provided you have the pypiwin32 module installed.
 * Tray icons have been modified to be easier to distribute under debian (DFSG compliant).
 * New versions are now checked against the Github releases page.
 * NowPlaying: MPRIS should now be used for Rhythmbox.
 * The MacOS port has been dropped since nobody will step up and maintain it.
 * The pseudo transparency (translux) feature has been removed.
 * Blinking of the trayicon is not recommended and has been removed.
 * Menu icons have been dropped since they are deprecated by GTK.

### Features

 * Translations works on Windows.
 * UPnP support out of the box on Windows.
 * Refreshed icon and GTK2 theme on Windows.
 * Gives user the option to load more than 1000 previous chat lines when they rejoin a chat room.
 * Virtual share system implemented.
 * You can now browse your buddy shares via the Share menu.
 * You can now rename your buddy virtual shares via the settings window for shares.
 * Plugins: can now be toggled on/off.
 * Plugins: a reddit plugin has been added.
 * NowPlaying: XMMS Infopipe support has been removed in favor of xmms2.
 * NowPlaying: BMPx support has been removed.
 * NowPlaying: Lastfm support has been updated and require an API key.
 * NowPlaying: Banshee support has been updated.
 * NowPlaying: Foobar support has been updated.

### Issues closed on GitHub

 * Question - Nicotine Still Being Developed? ([#1](https://github.com/nicotine-plus/nicotine-plus/issues/1))
 * bug in userbrowse.py ([#2](https://github.com/nicotine-plus/nicotine-plus/issues/2))
 * Remove max length on settings password field ([#5](https://github.com/nicotine-plus/nicotine-plus/issues/5), [#7](https://github.com/nicotine-plus/nicotine-plus/issues/7))
 * Randomly kill connections on select() out of range failure ([#6](https://github.com/nicotine-plus/nicotine-plus/issues/6))
 * Fix shares build / crashes caused by bogus metadata ([#10](https://github.com/nicotine-plus/nicotine-plus/issues/10))
 * UPnP Port Mapping piles up in the router ([#11](https://github.com/nicotine-plus/nicotine-plus/issues/11))
 * Currently broken on windows ([#18](https://github.com/nicotine-plus/nicotine-plus/issues/18))
 * File transfers are failing ([#19](https://github.com/nicotine-plus/nicotine-plus/issues/19))
 * Fix variable bitrate detection for MP3 files ([#20](https://github.com/nicotine-plus/nicotine-plus/issues/20))
 * Information On nicotine-plus.org ([#21](https://github.com/nicotine-plus/nicotine-plus/issues/21))
 * Build fails on archlinux, can't copy mo file... ([#22](https://github.com/nicotine-plus/nicotine-plus/issues/22))
 * Hidden directory files now showing up in file shares (Windows) ([#23](https://github.com/nicotine-plus/nicotine-plus/issues/23))
 * upnp functionality is used despite being config'd as False ([#24](https://github.com/nicotine-plus/nicotine-plus/issues/24))
 * userbrowse coredump on GTK 2.24.30+ ([#25](https://github.com/nicotine-plus/nicotine-plus/issues/25))
 * "invalid operation on closed shelf" error on every download ([#27](https://github.com/nicotine-plus/nicotine-plus/issues/27))
 * Unable to save settings ([#32](https://github.com/nicotine-plus/nicotine-plus/issues/32))
 * Clear Finished/Aborted button problem ([#33](https://github.com/nicotine-plus/nicotine-plus/issues/33))
 * Settings window slow to open ([#36](https://github.com/nicotine-plus/nicotine-plus/issues/36))

### Issues closed on Trac

 * "Abort & Delete" button is mislabeled (#194)
 * No icon found in nicotine.exe (#512)
 * French translation and non-translatable strings (#524)
 * Limiting number of upload slots doesn't work all the time (#651)
 * Add option to override locale dir (#495)
 * File and Fast-Configure keyboard shortcuts are the same (#658)
 * Rescanning shares stalls/fails in some cases (#671)
 * Distressingly, /al is not working in private chat (#678)
 * tab completion of user name does not work in private chat (#679)
 * slskmessages.py:69:__init__:Exception: Programming bug (#697)
 * upload queue size limits can't be set to "unlimited" (#706)
 * Impossible to install nicotine without a mouse (#712)
 * Tray icon is lost after explorer is terminated, doesn't return after explorer is restarted (#715)
 * nicotine crashed with TypeError in PopulateFilters(): value is of wrong type for this column (#726)
 * Dont draw eventbox background for tab labels (#727)
 * Rythmbox Now Playing Error (#750) (#935)
 * Realpath / filename error (#776)
 * Connection limit (#802)
 * Disabled UPnP support due to errors Message (Can We Silence?) (#803)
 * English text refactorizationillisms (#828)
 * Cannot download from soulseekqt users (#912)
 * Corrected Hungarian translation for 1.2.16 (#923)
 * Nicotine+ 1.2.16 on win7SP164bit - German language (#998)

 A bunch of outdated bug reports have been closed on Trac.


## Version 1.2.16 (October 31, 2010)

### Behaviour

 * Updated most country flags (#599)
 * All messages should now be properly timestamped in the log (#602)
 * Saving user pictures now appends a timestamp so pictures aren't overwritten

### Features

 * Foobar support for NowPlaying (#644)

### Bugs

 * Division-by-zero errors broke transfers (#561)
 * Some packets were packed incorrectly (#570)
 * Recursive downloads didn't work (#571)
 * Search results were improperly formatted (#594)
 * Copying folder URLS didn't work (#574)
 * Mid sentence tab completion destroyed input (#562)
 * Portmapping with MiniUPnPc (the binary) didn't work (#593)
 * Deprecated raise statements using strings (#613)
 * Transparency wasn't saved properly (#615)
 * Shares didn't work properly with out-of-ASCII characters (#623, #345)
 * Fileshare counter increased on refreshing a filelist (#617)
 * Program failed to start with a corrupt transfer file (#628)
 * Network loop crashed on invalid DistribSearch packets
 * Private rooms often didn't show up in the room list (#641)
 * nicotine.desktop was missing P2P and Network sub categories (#660)


## Version 1.2.15 (February 16, 2010)

### Behaviour

 * Changed the description for our .exe files so it shows up as Nicotine+ in
   firewalls (ticket #498)
 * When using an upload slot limit, uploads that don't start within 30 seconds
   are no longer counted as a used slot. This stops a single faulty user from
   preventing other connections
 * The clear button in the upload view now clears erred transfers too
 * Unhide user info tab when a new userinfo is received
 * Transfer views update less frequently reducing the amount of CPU needed.
 * xdg-open is now used by default to open folders and play music

### Features

 * Now-Playing support for Amarok2 (Ticket #423)
 * FastConfigure dialog for new users (Ticket #482)
 * Country flags now have tooltips (Ticket #521)
 * Now-Playing support for Banshee

### Bugs

 * Collapse mode in upload/download didn't work for newly added files, wasn't
   remembered with restart (ticket #205)
 * The packing/unpacking of network messages has been made more explicit. This
   should make Nicotine+ less likely to fail on different processor types and
   operating systems (Tickets #486 #493 #518 #540 #548)
 * Double quotation marks weren't filtered from filenames on Windows systems
 * Ban list got unintentionally deleted sometimes (Ticket #519)
 * "Show IP" didn't not work on the userinfo page (Ticket #522)
 * Wishlist searches would stop working if the setting "Reopen search tabs" was
   disabled and the user closed the search tab (Ticket #552)
 * Incoming RoomSearch raised exceptions

### Translations

 * \>\<((((*\> updated the French translation
 * djbaloo updated the Hungarian translation


## Version 1.2.14 (October 4, 2009)

### Behaviour

 * A corrupt configuration file will no longer make Nicotine+ fail on startup (ticket #483)
 * Multiple shares can now be loaded from the harddrive at the same time

### Features

 * Support for UPnP through MiniUPnPc (ticket #230)

### Bugs

 * Search failed to work on certain combinations of OS and processor (ticket #486)
 * Implemented our own filelist iterator, dramatically reducing the amount of
   CPU cycles needed to open filelists. Thanks goes to Nick Voronin (ticket #480)
 * Bitrates for Musepack audio were scanned incorrectly
 * Saving file lists from users with slashes in the name didn't work
 * Filesize was incorrect for files around 2 gigabytes and up in userbrowse.


## Version 1.2.13 (September 22, 2009)

### Behaviour

 * Download queue is stored independently from the normal configuration file (ticket #467)
 * Non-working connections are cleaned up more aggressively (ticket #473)

### Features

 * Themes can now use a range of image types, including SVG
 * Ownership of private rooms is now displayed
 * Search chatroom logs by pressing F3
 * ASF Support in case Mutagen is used
 * The location of Nicotine+ is restored on startup
 * Rudimentary download rate limiter
 * The NowPlaying code for Audacious now supports audtool2 as well

### Bugs

 * Notifications failed when a user had <> in the name
 * Highlight icon kept on blinking with detached windows
 * Fixed links in the Help menu that didn't work (ticket #459)
 * A few different GUI related bugs that should make Nicotine+ much more
   responsive and use less CPU: Startup time reduced when there is a queue,
   queueing many items at a timer, pressing buttons like "Clear Finished" and
   "Abort User's Upload(s)"
 * ...and lots of tiny bugs

### Translations

 * Žygimantas updated Lithuanian translation
 * Kenny updated Dutch translation
 * Nils updated Hungarian translation


## Version 1.2.12 (May 26, 2009)

### Behaviour

 * RGBA mode is no longer on by default, to use it pass the --enable-rgba flag when starting Nicotine+
 * On Windows, configuration files are now stored in the user's Application Data folder instead of the installation folder (bug #330)
 * The configuration screen for shares has been rearranged in order to make it more logical (bug #341)
 * Support for Mutagen has been added. This will result in more accurate information about bitrates and lengths (bug #259)
 * Icons have been replaced, the alt-tab icon is increased.
 * Most external calls now support pipes
 * Improved German (bug #394) and French translation (thanks goes to \>\<((((*\>)
 * The dependency for PyVorbis has been removed in favour of Mutagen (bug #409)
 * Notification popups will no longer stack but a single popup will be updated

### Features

 * Built-in Webbrowser (MozEmbed)
 * Ignore by IP
 * Windows components have been improved
 * The language selection now uses normal names instead of abbreviations (bug #332)
 * When switching languages GTK will be translated as well
 * Hash checking to eliminate duplicates. When a file name conflict arises after a download finishes both files are hashed
   to make sure the new file is not identical to the old one.
 * Public Room support has been added
 * The amount of tracked and displayed search results is now limited, which should allow nicotine+ to cope better with overly
   generic search terms. Internally a maximum of 1500 are recorded, of which a maximum of 500 are shown. The other 1000 can be
   retrieved by using the filters. (bug #284)
 * Notebook tabs can be reordered and hidden, and these settings will be remembered.
 * Search results are now limited. There are two different limits:
   1) The show limit. This is the amount of results shown in the search tabs
   2) The store limit. This is the amount of results stored internally. This is useful when using search filters
   These limits are configurable from the configuration screen. (bug #284)
 * Nicotine tries to rename itself from 'python' to 'nicotine' for programs like 'ps' (requires procname module) and 'pkill' (bug #355)
 * 'Remember choice' option in the quit confirmation dialogue
 * It is possible to ignore people based on their IP address
 * Import warnings are now shows in the log window as well as in the console (bug #381)
 * New logging functionality, which means no more messages should get lost in the console
 * You can change your password now (bug #424)
 * Misc. improvements to transfer handling
 * Tab completion can be done by in-line replacement instead of dropdown list
 * Transfer views now have a 'Place in line' column

### Bugs

 * The Danish translation is now stored under 'da'
 * Fixed sorting of percentage (bug #322)
 * A number of typographical errors have been corrected (bug #334 and #335)
 * When disabling sound this setting will be loaded correctly now (bug #285)
 * Repaired sayprivate function from the pluginsystem
 * The Windows versions now comes with jpeg62.dll (bug #342)
 * The word '-' is now filtered from search queries (bug #367)
 * Handling of word wrapping of extremely long words is improved
 * Tray icon menu on OSX
 * Private Room handling has improved (bug #432)


## Version 1.2.10 (December 30, 2008)

### Features

 * Added support for RGBA, enabling Murrine users to use transparency and round menus
 * Tabs can be reorderen and can be hidden

### Bugs

 * Fixed bug #177, notification popups are now split into file and directory notifications
 * Fixed bug #274, cancelling and disowning private rooms bug (fr3shpr1nc3)
 * Fixed bug #226, file size dropdown in search filters are more readable now
 * Fixed bug #310, activity icon no longer activates on our own typing
 * Timestamps in private messages now are displayed correctly
 * Room searches work again (was broken in 1.2.10alpha)


## Version 1.2.10 Alpha (November 9, 2008)

### Features

 * Added last.fm to the now-player (gallows)
 * Added first version of the plugin system
 * Tabs can be closed using the middle mouse button
 * Usernames can be copied from the channel list (right click, select the
   username from the menu)
 * Added a popup that will inform users in case a local port cannot be bound
 * Connections will be dropped when the maximum is approached, decreasing the
   chance for "IOError" messages

### Bugs

 * 'Send to player' failed because of missing quotes for finished downloads
 * Fixed a bug with tuple error message causing a traceback
 * Fixed a translation bug, caused by tabs positions top, left, etc that caused
   settings dialog to not work properly
 * Fixed rhytmbox support with "Now Playing" (gallows)
 * Fixed Audacious support with "Now Playing" (gallows)
 * Fixed sending out the wrong username with search results
 * Updated all server references to the new server
 * A inverted port range no longer causes connection failures
 * Removed deprecated GTK calls

### Buddylist

 * Radio buttons now allow the buddylist to be toggled as always visible, in own
   tab, or in the chatroom tab.

### General Changes

 * The Edit menu has been broken into Edit, View and Shares menus
   (similar to Enr1X's patch http://nicotine-plus.org/ticket/231 )
   Also fixed the duplicate Alt-B hotkey (hide flags is now Alt-G).
 * Committed QuinoX's patch for case-insensitive nick completion (#252)

### Chat Rooms

 * Added Server Message 141, enables Private Chat Room Invitations and thus
   allows those you invite to get past the annoying server message that warning
   when a user you've invited 'hasn't enabled private room add'.
 * Blocking a user's IP address is now easier with the addition of a chatroom
   popup menu item
 * Private Rooms: You can now create private rooms via the roomslist popup menu
   and add users to your private rooms via any chatroom user popup-menu. You can
   also drop ownership of a private room and drop membership of another person's
   private room. This feature is currently available on the testing server only.

### Search

 * Country flags are shown in search results, metadata dialogs

### Settings

 * Upload and Download transfer lists now have customizable double-click options
   in Transfers->Events.
 * A Backup config menu item was added to the Edit menu. This will backup your
   Nicotine+ config and config.alias (if it exists) into a BZ2 archive. If you
   cancel the backup filename saving process, an archive with the format
   'config backup YYYY-MM-DD HH:MM:SS.tar.bz2' will be created.
 * Visible colors have been added to the Colour settings (for those who don't
   read hexadecimal).
 * Separate fonts for Search, Transfers, Browse and a font for all other lists
   can now be set.

### Translations

 * Slovak Translation Updated (Jozef)


## Version 1.2.9 (September 22, 2007)

### Licensing

 * Relicensed all code under GPLv3 and LGPLv3

### General Changes

 * Config menu items that were in the File menu moved to the new Edit menu
 * Added credits and license note to About Nicotine dialog.
 * Disable many widgets (entries, buttons, lists) when disconnected from server
 * User tabs have right-click popup-menus in private, userinfo and userbrowse.
 * libnotify support added (patch by infinito ticket #176 )
   notification-daemon, libnotify and python-notify required
 * Added a 10 second cooldown between responding to Userinfo and Usershares
   requests from the same user (to mitigate damage from DOS attacks and simple
   accidents)
 * Notification text on tabs can be colored
 * Notification icons on tabs can be disabled
 * Close buttons on tabs no longer forced to 18x18px
 * Close buttons are dynamically added and removed when toggled in settings
 * Added global unrecommendations list
 * Merged Amun-Ra's 'Country flag column in Chatroom userlists' (this is a new
   feature on the testing server) but works with manual IP lookups with GeoIP.
   This requires the 242 flag images. Additions to several server messages are
   used instead of GeoIP if they are available.
 * Simplified GeoIP module loading

### User Info

 * Added popups to user's interests lists (search, add and remove interests)
 * Added a zoom and save popup menu to the Userinfo image.

### Shares

 * Shares are precompressed, before they're sent (Nicotine will recover faster
   from many shares requests)
 * Unicode filenames on Win32 are now read and shared properly (should be)

### Settings

 * Tooltips can be disabled
 * Settings widgets will now be colored red if their values are invalid.
 * Your client port and server-reported IP address are shown in Server Settings
 * Added an option to Shares for the Upload directory path (needs to be set)
   The upload directory is where your buddies 'uploads' will be saved.
 * Default colours and clear colours buttons added
 * All Notebook Tabs can be repositioned and the labels can be rotated 90⁰
   under Settings->Interface->Notebook Tabs
 * Added Exaile to NowPlaying
 * Added a config option for overriding the default language
 * URL handlers settings rearranged slightly, combo items in the handlers column
 * Rearranged the Settings tree and removed some descriptive panes
 * Added IP blocking and range blocking with * character
 * Some Entry widgets in settings replaced with SpinBoxes
 * Userinfo settings now have size data for image
 * New options to to determine what happens when destroying the main window
   (show a dialog, close to tray, or quit)

### Search

 * Search is now a genuine TreeView that supports group-by-user and
   has a expand/collapse all toggle when grouping is enabled.
 * Added a Clear results button
 * Added 'Download containing folder(s) to..' to the search results popup
 * Open a new socket for every outgoing search result to avoid problems with
   shared sockets getting closed.
 * Only close sockets of incoming search results if input/output buffers are
   empty. (this may still result in the transmitting sockets)
 * Added Search and Open Directory items to the uploads popup menu
 * Search results encoding improved (user's encoding, falls back to global)
 * Search results turn red when a user goes offline (configurable)
 * Added a 'multiple users' submenu to search results popup

### Transfers

 * Show total time elapsed and remaining in user's parent row instead of the
   current transfer's time elapsed and time remaining.
 * Added a maximum files-per-user limit to the upload queue
 * Added a 'Clear Failed' item to the uploads menu
 * Added 'Clear Filtered' and 'Clear Paused' to the downloads menu
 * Fixed pausing of aborted downloads after reconnecting to the server.
 * Added an 'Auto-retry Failed' checkbox to downloads (3 minute timer)
 * Added an 'Autoclear Finished' checkbox to uploads
 * Notify popups for completed files and completed directories (toggleable)
 * Added a 'multiple users' submenus

### Chat

 * Whitespace is now limited to two spaces
 * Show icon, sound, speech and title notifications for "current" chat tab
   if the window is hidden.
 * Notify popups for buddies with "notify" enabled :)
 * Read chatroom logs (and attempt to parse them) when rejoining a room.
   Parsing will not work if the logs do not use the default timestamp format.
   Chat room and Private chat logs are in separate sub-directories, now.
 * Threaded /aliases and /now commands (GUI no longer freezes)
 * Use the /detach and /attach chatroom commands to pop chatrooms and private
   chats into their own windows.
 * Text-To-Speech support added (configurable under Settings->Misc->Sounds)
   individual chat rooms can be disabled with the text-to-speech toggle button.
   Chat messages are read out, and nick mentions are announced. By default,
   there are commands for flite ( http://www.speech.cs.cmu.edu/flite/ )
   and festival ( http://www.cstr.ed.ac.uk/projects/festival/ ).
 * URL text color is configurable (doesn't effect old links after changing)
 * Timestamps are now configurable, disableable (under Settings->Chat->Logging)
 * Log files' timestamps are also configurable. Default is "%Y-%m-%d %H:%M:%S"
 * Added a help button for chatroom commands
 * Added hide/show buttons in chatrooms for userlist and status log. These
   buttons can be hidden by Edit->Hide chat room log and list toggles
 * Username away color-status in chat can be toggled off
 * Added Auto-Replace list (applies to all outgoing chat message text)
 * Added Censor list (applies to all chat message text)
 * A popup dialog appears after closing the last chat room while the roomlist
   is hidden.
 * URL's are now converted back to plain text by the URL catcher
   (before only %20 were converted to spaces)
 * Usernames in chat logs and private, userinfo and userbrowse tab labels are
   marked offline when disconnected from server
 * Ticker moved to the top-left of the chat room frame;
 * Added settings for tab completion and dropdown completion list
 * Added a completion dropdown list (gtk.EntryCompletion) to chat entries

### Bug Fixes

 * Re-enabled the 'if i.size is None' check which should fix some upload issues
 * Fixed a error message printed after aborting an upload directory popup
 * Fixed a major slowdown in needConfig function (was reading shares data)
 * Pressing enter in Search Filter entry boxes now works again
 * Readded "/" to pasted folder slsk:// URLs
 * Reading slsk.exe's cfg files should now work on Windows


## Version 1.2.8 (June 1, 2007)

### General Changes

 * Support for Spell Checking in chat added (libsexy and python-sexy required)
 * Other users Interests are now shown in the User Info tab, with expanders
 * Send Message added to trayicon
 * Popup Menus in Private, Chatrooms, and User Browse reorganized
 * The user-entry boxes are now buddy-list combobox entries
 * Users with PyGTK >= 2.10 will use the gtk.StatusIcon instead of
   the old trayicon.so module.
 * Added a filemanager popup item to the self-browse menu; configurable
   under Settings->Advanced->Events
 * Gstreamer-Python support for sound effects added
 * Added Soulseek testing server (port 2242) to the server combobox.
 * Changed the URL Catcher's syntax. The ampersand "&" is no longer needed
   at the end of URL Handlers. The handler entry is now a combobox and
   includes a bunch of webbrowser commands.
 * Userlist Columns are hidable and hidden status is saved.


### Transfers

 * Added a "Group by users" check box
 * Added Expand/Collapse all toggle button to transfers
 * Added a popup dialog to the "Clear Queued" transfers buttons

### Private Chat

 * Added gallows' patch for including your username in the private chat log.
   (ticket #161)
 * Direct private messages (currently only supported by Nicotine+ >= 1.2.7.1)

### Search

 * Search now has combo boxes, per-room searching and per-user searching.
 * Added Wishlist and changed remembered search tabs to only display
   when new search results arrive
 * Switch to newly started search tab (ticket #157)

### User Info

 * gallows added userinfo image zooming via the scrollwheel (ticket #160)

### Settings

 * Changed Audio Player Syntax it now uses "$" as the filename
 * Exit dialog can be disabled in Settings->UI
 * When a config option is detected as unset, print it in the log window.
 * Move Icon theme and trayicon settings to a separate frame
 * Move sound effect and audio player settings to a separate frame
 * Reopen Settings dialog, if a setting is not set.

### Networking

 * On Win32, hyriand's multithreaded socket selector is used. This will allow
   a larger number of sockets to be used, thus increasing stability.
 * Added Server Message 57 (User Interests)
 * Send \r\n with userinfo description instead of just \n

### Bug Fixes

 * Uploads to other Nicotine+ users work better
 * Userinfo Description does not scroll to the bottom of the window
 * Fixed a few bugs with the trayicon
 * Fixed server reconnection not actually trying to reconnect (and giving up
   on the first try)

### Translations

 * Lithuanian translation updated
 * Euskara translation updated


## Version 1.2.7.1 (March 6, 2007)

### General Changes

 * The About Nicotine+ dialog now shows the versions of Python, PyGTK and GTK+
 * Copy was added to the right-click menus in chat status and
   debug logs.

### Bug Fixes

 * The shares scanning progress bar now disappears after scanning shares a
   little more frequently.
 * Fixed a bug in the way total transfer slots were calculated
 * Improved Remote-Uploading somewhat (was quite buggy with two Nicotine+ clients)
 * Fix directory name cropping in 'upload directory to' in User Browse
 * Attempted to fix the 'interrupted system call' (which sometimes are caused
   by gtk+ file dialogs) from stopping the networking loop.
 * Username hotspots for users who are offline or have left the room aren't
   disabled anymore.

### Transfers

 * Downloads have a metadata popup dialog with bitrate / length
 * Right-clicking when nothing is selected will select a row
 * In parent row, display the current transfer's time elapsed and time left.
 * Transfer popups work better on parent rows

### Translations

 * Silvio Orta updated the Spanish translation
 * \>\<((((*\> and ManWell updated the French translation
 * nince78 updated the Dutch translation
 * Nicola updated the Italian translation
 * Žygimantas updated the Lithuanian translation


## Version 1.2.7 (February 25, 2007)

### General Changes

 * Window size is restored on startup
 * Background color of entry boxes, text views and list views is now changeable
   and all lists foreground color changes with the 'list text' option.
 * Added some padding around various widgets
 * Tabs can be reordered on the fly, now (Requires PyGTK 2.10) Also, Chat Room
   tab positions are saved in their reordered position.
 * Per-file indentation consistency was drastically improved. transfers.py,
   slskproto.py and a few others were really bad.

### Settings

 * Added an Import Config frame to Settings, which duplicates the functionality
   of nicotine-import-winconfig. User can now easily import config options
   from the official Windows Soulseek client's config directory. Support for importing
   the ignore list was also added to nicotine-import-winconfig.
 * Translux (pseudo-transparent TextViews) is an old easter egg that is now
   customizable in UI Settings.
 * Transfer settings was rearranged and organized with expanders
 * Transfer settings has a new combo box for selecting which users are allowed
   to initiate uploading files to you. Trusted users are set in the buddy list.
 * Added several tooltips to Settings' transfer widgets in hopes of providing
   better explanations of some of the more complex functionality.

### User List

 * Comments in Buddy List can now be edited in-list by clicking twice on the
   comment column, not by double-clicking (which would open Private Chat).
 * Trusted checkbox column added to the buddy list. Trusted users are an
   optional selection of users to whom remote uploads can be limited.

### Chat

 * Usernames in the chat room log now have hotspots associated with them,
   meaning they can be left-clicked on to load the same popup as you have in
   the users list.
 * Usernames are also colored based on Online, Away and Offline/In-Room status.
   This option can be disabled in UI Settings.
 * "User is away/online/offline" messages removed from Private Chat


### Transfers

 * Transfers are now sub-items in a one-step tree with the user as a parent
 * QuinoX's patch, a download filter: ( http://qtea.nl/tmp/nicotine+ ) was
   reworked a little and given a nice listview to add the Regular Expressions
   (filters) to. This feature will allow you to blacklist certain types of
   files, which may save you from the pointless downloading and cleanup of
   unwanted files.
 * Downloads and Uploads popup menus have a new item under the user submenu,
   "Select User's Transfers".
 * Uploads can be retried
 * The Size column now has the current file position and the total file size
 * Remotely-Initiated-Uploads will no longer be accepted if an Upload Queue
   Notification message has not been sent, first. This means versions of
   Nicotine+ earlier than 1.2.5 will not be able to initiate sending you files,
   no matter what your allowed uploaders is set to.

### User Info

 * Stats were rearrange and the status of who is allowed to initiate uploads to
   the user was added.

### User Browse

 * The browsetreemodels functions were disabled, and file and folder treeviews
   were reimplemented with code from the PyGTK2 museek client, Murmur.
 * Search now works slightly different. Queries match all files in a directory,
   and switch between matching directories each time.
 * Tree lines and a 'Directories' sorting header were added to the Folder Treeview
 * Upload Directories Recursive was added to Folders' Popup
 * An expand / collapse all directories button was added
 * Recursive downloads in User Browse now checks from > 100 files and displays
   a Warning dialog that gives you a chance to cancel downloading.

### Search

 * Search has a new popup window for displaying the metadata of search results.
   This popup is accessible after selecting 1 or more files and clicking on the
   "View Metadata of File(s)" popup menu item. From this window, you can also
   download file(s) or initiate browsing of the current file's user's shares.

### Networking

 * Handle all peer message unpacking with an exception handler. Should make us
   safer from malformed data sent by users.
 * Close peer connection when userinfo's or browse's close buttons are pressed.
   (This is to save bandwidth)

### Translations

 * \>\<((((*\> updated the French translation
 * (._.) and Meokater updated the German translation
 * nince78 updated the Dutch translation
 * Nicola updated the Italian Translation
 * Added Finnish translation by Kalevi
 * Added Lithuanian Translation by Žygimantas
 * Added Euskara (Basque) translation by Julen of librezale.org

### Bug Fixes

 * Various minor bugs killed
 * Userlist selection bug fixed
 * Fixed search results from last session being placed in search result tabs in
   new session that match their tickets by using random tickets instead
   starting from 0.
 * Fixed Big memory leak with PixbufLoader in Userinfo (call garbage collector)
 * Fixed large-file (>4GB) file scanning and shares browsing issue


## Version 1.2.6 (October 21, 2006)

### Interface Changes

 * Added a GUI for new built-in NowPlaying scripts and new /now command to use
   them. Supported players: Amarok, Rhythmbox, BMPx, XMMS/Infopipe, MPD/mpc.
   An 'other' player option also exists.
 * Added /buddy, /rem, unbuddy commands to Private Chat and Chat Rooms.
 * The Userinfo Picture file chooser now displays a preview of the image
 * Private Chat does not allow you to send messages while offline. New
   disconnected and reconnected messages appear in the chat log. Another new
   message is displayed if you were sent messages while offline.
 * Users' Shares lists can be saved to disk and then reloaded them, for ease
   and speed. On *nix, these files will be stored in ~/.nicotine/usershares/
 * Display shares-scanning errors in the Log Window
 * Added Titlebar messages on Private Chat and nick mention in Chat Rooms
 * Disabled: Urgency Hint on highlight (Titlebar flashes, or WM tries to get
   your attention) Doesn't work very well, disabled for now.
 * Popup a warning message if the Guide cannot be found
 * Added 'Copy all' menu item to Room Status logs and the debug log
 * Also added icons to the Clear log and the Remove Dislike menu items
 * Enlarged number entry boxes in Transfer Settings
 * Added thread protection to File/Directory Chooser (was getting freezes)

### Search

 * Search's Close button also "ignores" the search, like the X button the tab.
 * Fixed bug in "Download file(s) to..." causing the path to be corrupted.

### Config

 * Use a safer method to save the config file. Create 'config.new', move old
   'config' to 'config.old', rename 'config.new' to 'config' (from 1.1.0pre1)

### Packaging

 * Added 4 nicotine-plus-??px.png icons 16px, 32px, 64px and 96px.
 * nicotine.desktop and nicotine-plus-32px.png are installed to
   $PREFIX/share/applications and $PREFIX/share/pixmaps

### Windows

 * Added elaborate Unicode filename-reading hack. This should allow
   non-latin files/directories to be added to the shares. (Since this feature
   breaks in Linux, Windows detection is used throughout the filescanner
   converting strings to unicode and back.
 * Always load dbhash module on Windows

### Networking

 * Re-enable Server Ping (120 sec) and Timeout for Connection Close (120 sec)
 * Spoof warning now includes the IP and port of the user sending the message.

### Tray Icon

 * Hacked apart Systraywin32 from Gajim to work with Nicotine+ on Windows
   requires pywin32 which you can download from here:
   http://sourceforge.net/project/showfiles.php?group_id=78018
 * Fixed a bug with the Trayicon initially being icon-less

### Translations

 * Hungarian translation updated (djbaloo)
 * Portuguese-Brazilian translation finished (SuicideSolution)
 * Slovak Translation Updated (Jozef)


## Version 1.2.5.1 (September 18, 2006)

Bugfix release

 * Made TrayIcon not attempt to load on 'win32' operating systems
 * Fixed trayicon bug that caused error messages every time the Settings
   window's Apply or Okay button was pressed when the trayicon isn't loaded.
   (reported by renu_mulitiplus)
 * Fixed displaying your own Userinfo image on Windows.
 * Replace the characters ?, ", :, >, <, |, and * with an underscore _ on
   Windows, to avoid filesystem errors. (Reported by theorem21)
 * Made the Directory Chooser start with the predefined directory set.


## Version 1.2.5 (September 17, 2006)

### General Changes

 * Made columns reorderable (temporarily, they return to the default order
   after a restart)
 * Made the encodings Comboboxes give location or language details in a
   separate column.
 * Made all the popup menus have GTK stock icons.
 * Made most of the Main Menu items have icons.
 * Added three new menu options under help: Offline Nicotine Plus Guide, the
   Nicotine-Plus Trac and the Nicotine Plus Sourceforge Project websites.
 * Added the NicotinePlusGuide to setup.py, so it will be installed
 * Set Firefox as the default http:// URL handler
 * Replaced "pure text" percent column with a CellRendererProgress column in
   the Downloads and Uploads transfer lists.
 * Added option to UI Settings to show/hide the transfer buttons.
 * Added expander to glade2py, so it can now be used.
 * Rearranged the new user entry/buttons to the top left of their tabs, added
   spacing inside tabs.
 * Added more stock GTK icons to Settings and Userinfo, among other places.
 * Added confirmation exit popup dialog when quitting with the window manager.
 * Made the main window's minimum size to be 500x500 px

### Bug Fixes

 * Fixed a typo in transferlist.py that caused some transfers to get stuck
   in the Initializing state, even though transfers still work.
 * Fixed the Chatrooms tab hilite bug (reported by Offhand, xrc)

### Tray Icon

 * Made the Tray Icon's popup menu disable menu options based on connection
   status. Also simplified its code to match the way Nicotine normally
   creates menus.
 * Made Trayicon toggleable while running from the UI settings or at startup
   with --enable-trayicon, -t  and --disable-trayicon, -d

### Search

 * Made /search commands modify the search history
 * Added 'clear search history' button to search
 * Shortened Search tab length and added a label containing the full query
   next to the "Enable filters" checkbox.

### Audio

 * Notifications: Now testing 'flite' support, a text-to-speech engine.
   This may or may not be removed. The option is 'speechenabled'
 * Moved Icon theme and Sound theme settings inside separate expanders.
 * Notifications: Added a sound effect, room_nick.ogg, for nick-mention in
   chatrooms (when not in that room) and a separate sound effect, private.ogg,
   for when a private message arrives, and you are not in that tab. Sound
   options are found in the UI settings, and separate sound theme directories
   and audio players can be selected, as well. Ogg files are installed into
   $PREFIX/share/nicotine/$THEMEDIR/

### Networking

 * Added support for sending and receiving Soulseek peer message 52, Upload
   Queue Notification, which allows users to notify upload recipients that
   they are attempting to send a file. Also, a log message is printed when a
   user attempts to send you file(s) and an automatic is sent if they aren't
   allowed to.
 * Add a Bool to the GetUserStatus message received from the server, for
   privileges. If 1, add user to list of privileged users.
 * Added SendUploadSpeed (121) message which replaced SendSpeed (34) a long
   time ago. Thanks to sierracat for the info, and to slack---line for testing.
 * Modified CheckVersion function to allow for milli ( X.X.X.X  ) versioning.


## Version 1.2.4.1 (August 18, 2006)

Bugfix release

 * Disabled use of 'pwd' module on windows
 * Fixed bug with Buddylist tab not appearing on startup.
 * Fixed bug with double-clicking on a user in the Buddy not switching to the
   correct private chat tab.


## Version 1.2.4 (August 17, 2006)

 * Added new translations for Hungarian (djbaloo) and Slovak (Josef Riha)
 * Made Buddylist toggleable between its own tab and pane on the right side
   of chatrooms
 * Rearranged tabs to the top of the window
 * Rearranged Browse Share's progress bar as in Ziabice's patch
 * Added a Font selector for chat messages under Settings->UI->Interface
   (47th_Ronin's request)
 * Made Nicotine's shares builder ignore ALL dot-files and dot-directories
   (such as the ~/.nicotine/ directory) for security reasons. (Izaak's idea)
 * Warn if home directory is being shared. (Izaak's idea)
 * Added the First in, First out queue from jat's evil cocaine patch (without
   any of the other features)
 * Added gtk stock icons to many buttons
 * Added user entry boxes in Private Chat, User info, and User browse
 * Added new birdy icons which replace the little people icons
 * Added a theme selector to Settings->UI->Interface->Icon Theme Directory
   If any of the theme icons exist in this directory, they'll be used instead
   of the built-in images.
 * Made Copy URL popup menu options use the ctrl-c/ctrl-v clipboard, as well as
the middle-click one
 * Split big Download/Upload Popup menus into submenus
 * Fixed an problem with upload percentages not working properly


## Version 1.2.3 (July 7, 2006)

 * Added abort, retry, ban, clear queued, and clear finished/aborted buttons
   to transfers.
 * Made lists' rows to use the alternating color pattern.
 * Changed all the icons. Most of the new icons are modified from
   Mark James' Silk icon set: http://www.famfamfam.com/lab/icons/silk/
 * Fixed other users sending PM cause the tab to be switched to their message.
 * Fixed erroneously translated internal strings that caused queued downloads
   to fail.


## Version 1.2.2 (June 15, 2006)

 * Renamed "User list" to "Buddy list"
 * Added Double-clicking on a user starts a private message in the chatrooms,
   the userlist, and similar users.
 * Added TrayIcon from unreleased Nicotine 1.1.0pre1, and added a menu to it.
   This is a module and needs to be compiled.
 * Added Speed, Files and Dirs to userinfo
 * Made more strings translatable
 * Added Buddy-only shares


## Version 1.2.1 (June 10, 2006)

 * Added a bunch of hotkeys to the popup menus and normal menus.
 * Added a new menu for Modes (Chat Rooms, Private Chat, etc)
 * Starting a Private message via the Popup menu will now switch you Private
   Chat tab, so you can immediately start typing.
 * Fixed a segfault in User Browse, if you clicked on the folder expanders while
   shares were loading. This was done making the folder pane be disabled while
   refreshing.
 * Updated translations to work with hotkey menu and other changes
 * French translation: systry corrected typos and translated more strings.
 * Added a Send to Player popup menu item, which allows you to send downloading,
   uploading or files in your own shares to an external program, such as a media
   player.


## Version 1.2.0b (May 11, 2006)

 * Added a "Send to Player" popup menu item for downloads and personal shares


## Version 1.2.0 (May 10, 2006)

 * Added New Room and User search messages, and use them instead of sending out
   direct peer searches
 * Fixed all those depreciated Combo() functions, updated all of them to
   PyGTK 2.6 compatible functions.
 * Fixed the CRITICAL pygtk_generic_tree_model warning that has been plaguing
   Nicotine since GTK2.4 came out. The problem was fixed by adding:
   "if not node: node = self.tree"  to the on_iter_nth_child() function.
 * Moved the upload popup-menu item so that it isn't incorrectly disabled from
   sending multiple files.
 * Added two new debugging messages for when someone browses you or gets your
   userinfo, you can see their username. ( Idea/code stolen from "Airn Here",
   pointed out by heni (thanks to both of you) )
 * Fixed a little bug in a popup menu that caused a traceback
 * Added an optional client version message, which is similar to the CTCP
   VERSION message on IRC. It sends your client's version via Private Message to
   a remote  user. You can disable automatic responding of it in the
   Settings->Server.  So far, it works only with this version of Nicotine and
   Museek's Curses client, Mucous. Send it via the popup menu in Private chat,
   or with the command: /ctcpversion


## Version 1.0.8-e (March 25, 2006)

 * Made password to be starred like ***** via cravings' patch
 * Added a Give Privileges popup menu item (taken from the development 1.1.0pre1
   version of nicotine that hyriand never released.)
 * Changed the Upload Files dialog from a textentry to a scrollbox


## Version 1.0.8-d (August 17, 2004)

 * 1.0.8-d is a combo of 1.0.8z and some new stuff, listing it all here.
 * Added GTK2-Fileselector (Works nicely for Win32)
 * Added many changes to wording of the settings dialogs
 * Added Remote Uploads (Browse yourself, right click on files, upload, type in
   username)
 * Added Remote Downloads (Added Checkbox in Settings->Transfers)
 * Fixed some of the many PyGTK warning messages
 * Removed the PING-OF-BAN


# Release Notes (Nicotine)

## Version 1.0.8rc1 (May 1, 2004)

 * Added the missing handler for server-pushed searches
 * Allow users to have negative speed-ratings
 * Double click downloads in searches and browsers, join room in room list


## Version 1.0.7 (January 11, 2004)

 * Changed hate-list to be network-driven instead of being a filter
 * Updated translations
 * When available, Nicotine will use PyGNOME to launch protocols that
   haven't been configured


## Version 1.0.7rc2 (January 7, 2004)

 * Moved encoding dropdown-list out of the scrolled area in userinfo tabs
 * Transfer logs (enable in settings->logging)
 * Last 7 lines of a private message log are shown
 * Config file now backed up (to \<filename\>.old)
 * Check privileges shows days, hours, minutes, seconds
 * Changed default server to server.slsknet.org
   (mail.slsknet.org will be automatically changed)
 * Anti-frumin ticker update (replace newlines with spaces)
 * Added country-code filter to the search filters
 * Added a "Hide tickers" menu entry which hides all tickers
 * Added option to not show the close buttons on the tabs
 * Added option to not lock incoming files
 * Fixed /tick


## Version 1.0.7rc1 (January 2, 2004)

 * Added room ticker support
 * Alt-A fixed


## Version 1.0.6 (December 5, 2003)

 * Probable fix for GUI freeze (thanks stillbirth)
 * Bye bye total queue limit
 * Translations updated


## Version 1.0.6rc1 (November 18, 2003)

 * Files that are downloaded should now be encoded
 * Possible fix for a threading race condition
 * Possible fix for listport not defined problem and a million little things
 * Possible fix for yet-another-corrupted-shares-database problem
 * Translation caching
 * Whacked some tracebacks
 * Implemented recommendations system
 * Translation updates
 * Added polish translation (thanks owczi)
 * Fixed bug that made "Queue limits do not apply to friends" not work
 * Fix for the version checking bug


## Version 1.0.5 (November 7, 2003)

 * Quickfix for protocol change


## Version 1.0.4.1 (September 26, 2003)

 * Changed default server
 * Fix for online notify
 * Added french translation (thanks flashfr)


## Version 1.0.4 (Sepember 17, 2003)

 ---> Can you find the EASTER EGG? <---

 * Show IP address now shows country name instead of code (when GeoIP is
   installed)
 * Fixed sorting in transferlists
 * Clear (room) log window popup menu
 * Room and user encodings (for chats, browse, userinfoetc)
 * Close buttons on sub-tabs
 * Translatable (see the languages/nicotine.pot file)
 * Window icon (normally blue, yellow when highlight)
 * MacOSX OSError / IOError fixups
 * Fix for minimum window size
 * Desktop shortcut (files/nicotine.desktop), not installed by default
 * Possible fix for the "ServerConnection doesn't have fileupl" problem
 * Userinfo is now properly network encoded
 * Bundled a custom version of the ConfigParser that doesn't have problem
   with semi-colons
 * Download to.. for searches now defaults to downloaddir
 * Close tab-button for searches closes and ignores
 * UTF8 log window fixes
 * Fix for invalid server traceback (in settings window)


## Version 1.0.3 (August 28, 2003)

 * PyGTK version check (Nicotine requires 1.99.16 or higher)
 * Hide room list menu option (is remembered between sessions)
 * Control-C doesn't kill nicotine anymore (silently ignored)
 * Fix for deprecation warning (PyGTK 1.99.18)
 * Bug-reporting assistant (based on work by
   Gustavo J. A. M. Carneiro)
 * Reduced the sensitivity of the auto-scroller a bit
 * Workaround for missing-menu-labels in tab popup menus
 * Changed PyVorbis warning
 * Check latest (checks if you're using the newest version)
 * Autocompletion of / commands
 * Some small psyco fixes
 * Browse yourself without even being connected
 * Default filter settings
 * Fixed searches for special characters and limit history to 15 entries
 * Long overdue enter-activates-OK in input dialog
 * Make folder button in directory chooser dialog
 * Change %20 in slsk:// urls to spaces (blame Wretched)
 * Copy file and folder URLs in transfer lists and searches
 * Fixed Hide log window on startup
 * Improved the move-from-incomplete-to-download-folder function so that it
   can move across partitions / drives / whatever.
 * Now really included Carlos Laviola's debian control files


## Version 1.0.2 (August 23, 2003)

 * Possible fix for freezes
 * Fix for GTK-Critical at startup with hidden log
 * Fixed URL catcher regular expression a bit
 * Added debian control files (by Aubin Paul)
 * Hopefully fixed the missing "2 chars search result directory" thing
 * Fixed roomslist popup menu
 * More UTF8 cleanups (and dumped the need for most of the localencodings
   in the process), should really work on MacOSX again
 * Fixed alt 1-8 / left,right,up,down to work with numlock / scrolllock on
 * Checkboxified all the "Add to user list", "Ban this user" and "Ignore
   this user" context-menu items
 * Fixed small bug in config loader (concerning importing pyslsk-1.2.3 userlist)
 * Fixed small bug in the browse file model
 * Fixed some selection issues
 * Fixed rooms list being sorted A-Za-z instead of Aa-Zz
 * Fixed column-sizes being weird when resizing
 * Removed talkback handler
 * Added handler for slsk:// meta-protocol and the ability to copy slsk://
   urls in browse ("Copy URL").
 * Should work on OSX again
 * Threading issue with rescanning fixed
 * Focus chat line input widget on tab change (chat rooms and private chat)
 * \<insert stuff I forgot to add to changelog here\>


## Version 1.0.1 (August 19, 2003)

 * UTF8 fixes for settings window
 * UTF8 fixes for directory dialog
 * UTF8 fix for private chats in some locales (fr_FR for example)


## Version 1.0.0 (August 18, 2003) (Initial Public Release)

 * Changed URL to the Nicotine homepage to http://nicotine.thegraveyard.org/
 * Added Alt-H accelerator to hide log


## Version 1.0.0rc8 (August 18, 2003)

 * New MP3 header engine (shouldn't crash anymore, and should be faster)
 * Made the default handler for the http protocol more compatible (added
   quotes)


## Version 1.0.0rc7 (August 17, 2003)

 * Fixed check privileges (thanks hednod)
 * Userlist context menu issues fixed
 * Several win32 fixups / custom-hacks made for upcoming win32 release


## Version 1.0.0rc6 (August 16 2003)

 * Merged PySoulSeek 1.2.4 core changes
 * Privileged users in userlist
 * Online notify


## Version 1.0.0rc5 (August 16 2003)

 * pytgtk-1.99.16 compatibility fix (thanks alexbk)


## Version 1.0.0rc4 (August 16, 2003)

 * Fixed private-chat-shows-status-change-a-million-times
 * Fixed bug concerning GeoIP not being able to look up country code
 * Fixed email address in nicotine "binary"


## Version 1.0.0rc3 (August 16, 2003)

 * Geographical blocking works for search results too
 * Geographical blocking settings now automatically uppercased
 * py2exe.bat bundled (used to create a "frozen" .exe on win32)
 * setup.iss bundled (used to create an installer using InnoSetup)
 * Tab menus now show page title instead of Page n
 * More win32 fixups
 * URLs now only respond to left click
 * User-info description field in settings now wraps
 * User-info image no longer writes temporary image file
 * Image data now encapsulated in imagedata.py


## Version 1.0.0rc2 (August 13, 2003)

 * Fixed typo


## Version 1.0.0rc1 (August 13, 2003)

 * Nasty Bug(tm) fixed
 * URL catcher fixup
 * Server banner is now shown
 * Hide log window menu item
 * Win32 fixups


## Version 0.5.1 (August 13, 2003)

 * URL catching
 * Bugfix: /ip no longer shows None
 * Bugfix: CheckUser would fuck up when disconnected
 * Fixed date for 0.5.0


## Version 0.5.0 (August 13, 2003)

 * Geographical blocking using GeoIP (optional)
 * Userlist only sharing
 * Userlist values are reset after disconnect
 * Small bugfixes and typos
 * Instead of printing certain bugreports to the console,
   it now sends a private message to hyriand instead


## Version 0.4.9 (August 11, 2003)

 * Python 2,2,0 compatibility
 * Python 2.3 deprecation warning fixed
 * Minor bugfixes (mainly in transfer lists, I hope they work)
 * Fixed the setup.py to install images
 * Added browse files to search results context menu
 * Added abort & remove file to downloads context menu
 * KB/GB/MB is now done at 1000 instead of 1024 (producing 0.99 MB instead
   of 1000 KB)


## Version 0.4.8 (August 10, 2003)

 * Minor bugfixes and de-glitchifications


## Version 0.4.7 (August 9, 2003)

 * New logo and icon (thanks (va)*10^3)
 * Generate profiler log when using nicotine --profile
   (profiler log will be saved as \<configfile\>.profile)


## Version 0.4.6 (August 8, 2003)

 * Room user lists are filled again when reconnected
 * User is offline/away/online in private chats
 * Right-click on tab shows tab list
 * Auto-reply implemented
 * Added *1000 factor for auto-search interval *oops*


## Version 0.4.5 (August 7, 2003)

 * Page Up / Down scrolls chats
 * // at the start of a chat line will "escape" the / used by commands
 * Evil typos corrected (tnx SmackleFunky)
 * Bugfixes
 * Search filter history


## Version 0.4.4 (August 7, 2003)

 * Bugfixes
 * About dialogs


## Version 0.4.3 (August 5, 2003)

 * Small bugfixes (sorting, UpdateColours, ChooseDir)


## Version 0.4.2 (August 5, 2003)

 * First changelog entry.. Basically everything implemented :)


# Release Notes (PySoulSeek)

## Version 1.2.4 (August 16, 2003)

The final version

 * Workaround for corrupted shares database problem which many Mac users seem to
   have
 * Notification for incomplete configuration
 * Fix for a subtle race condition between starting transfers and getting a
   list of privileged users
 * It's now possible to give download privileges to users from the userlist
 * Password entry box now uses ***
 * Search responses are now buffered - less flicker, less stress on the client
 * If log window is collapsed, messages are now duplicated in the status bar
 * It's now possible to track status changes for the individual users from
   the userlist


## Version 1.2.3 (July 23, 2003)

### Added Features from Hyriand's Patch

 * Pyslsk will ping the server every 30 seconds (rewrote it to be
   gui-independent)
 * Search history (remembers 10 last searches)
 * Log window is now collapsible (state is remembered between sessions),
   rewrote it to look prettier than hyriand's version
 * Resizable panels aren't deleted anymore when made really small
 * Userinfo and browse tabs show user status
 * /clear /c will clear a chat screen
 * version in the window title

### Other Fixes

 * the default "queue if" limit is now 10 kb/s to avoid "how do I limit the
   number of uploads" questions
 * errors when decompressing filelists and search results no longer
   cause a crash
 * if locking a file is not possible, a download will continue anyway
   with a warning


## Version 1.2.2 (June 24, 2003)

 * wxPython 2.4.1 fixes; this version is now required, because it fixes
the "crash-on-tab in an empty notebook" problem and handles ctrl-c gracefully
 * Ugly but working fix for the "cannot install idle handler twice" crash


## Version 1.2.1 (June 18, 2003)

 * Python 2.3 fixes
 * Python 2.2.0 fixes
 * Fix for "too many open files problem"
 * Aborted files are now not restarted when a user logs back on
 * New address for postcards


## Version 1.2.0 (May 17, 2003)

 * Tweaks for reducing CPU usage


## Version 1.2.0pre4 (May 13, 2003)

 * Fix for silly queue bug
 * Split the file index into two - primary index of files and secondary index
   of words. This should improve performance.


## Version 1.2.0pre3 (May 12, 2003)

 * Fixes for transfer bugs


## Version 1.2.0pre2 (May 12, 2003)

 * Changing options without rescanning caused a traceback


## Version 1.2.0pre1 (May 12, 2003)

 * Per user upload queue limit (specified in megabytes)
 * Switched to bsd db for storing shared files information
 * Contents of unknown messages is now printed in the log window
 * Improved performance of searches lookup (should help with ui freezes)
 * Improved the (*) in window title behaviour


## Version 1.1.2 (April 29, 2003)

 * Fixed a race condition occurring on SMP machines
 * Added remembered/wishlist searches from Hyriand's patch
 * Fixed stuck "Requesting file"
 * Sometimes transfer timers were not cancelled properly


## Version 1.1.1 (April 28, 2003)

 * Improved transfer status messages
 * Fixed a couple of potential transfer problems


## Version 1.1.0 (April 26, 2003)

 * Removed all references to wxPythonOSX - it's too instable
 * Updated pyslsk-import-winconfig
 * Pressing OK in settings now disables the config window when a
   rescan is happening
 * Aborted downloads are now kept in the downloads list
 * When there's a new private message or a public message that contains your
   username, the window title is marked with a (*)


## Version 1.1.0pre5 (April 19, 2003)

 * Fixes for two embarrassing bugs in pre4


## Version 1.1.0pre4 (April 18, 2003)

 * Improved userinfo and userbrowse gauges behavior
 * Fixed a bug where index of shared files was corrupted
 * Fixes for some tracebacks introduced in pre3
 * Old index is not anymore used for building a new one, as it doesn't
   improve speed
 * If a user already exists in the userslist, adding him edits the comments
 * Messages from the networking thread are now printed in the log window, not
   on stdout
 * Fixed the 100% CPU usage problem that happened occasionally


## Version 1.1.0pre3 (April 17, 2003)

 * pyslsk now switches to the new server automatically, if the old one is
   found in the settings
 * File errors when transferring files are now reported in the log window
 * If a peer does not do a proper initialization procedure, the connection is
   closed
 * It was not possible to edit userlist comments
 * Updated OS X instructions


## Version 1.1.0pre2 (April 14, 2003)

 * The new more efficient distributed network is now supported
 * The server location is now hardcoded, still possible to correct it
 * Files in 'Cannot connect' state are now retried once, just in case the
   server forgot to tell us the user status
 * Added autojoin checkbox in room windows
 * If the logs directory does not exist, it is created
 * Config window is now non-modal
 * If status was set to away manually, auto-return does not happen
 * Sorting the userlist now works properly


## Version 1.1.0pre1 (April 5, 2003)

 * Code cleanups (with suggestions from Alexey Vyskubov)
 * Added ignore list (by SmackleFunky)
 * Added autoaway (with configurable timeout)
 * If the server reports port 0 for a user, try again, up to 10 times
 * Fixed stuck "Waiting for transfer"
 * Rescan on startup now happens in background
 * Userlist is now in its own tab, you can now add comments to entries
 * A private message is sent as a workaround for windows client bug
   with "download containing folder"
 * If a parent node in the distributed network starts sending garbage, close
   the connection and find another parent
 * File errors are now written in the log window, not on stdout
 * It is now possible to download two files with the same name simultaneously
 * If a file already exists, pyslsk does not overwrite it with a just
   finished file, it renames it to file.1 (file.2 and so on)
 * It is now possible to abort a transfer and remove the incomplete file
 * Added popup menu in private chat tabs
 * It is now possible to sort search list by order of arrival and by
   possibility of immediate download
 * Search and browse lists now have bitrate and length as separate columns
 * Menu items in transfers panels were not always working
 * Reduced flicker in the chatroom userlist
 * Queue sizes are now reported more accurately


## Version 1.0.4 (March 26, 2003)

 * If your name was mentioned in a chat room, the chat tab will be
   highlighted with a yellow bird, not with the blue one. Also, the line
   containing  your username will be red. (based on patch from Hyriand)
 * pyslsk now sends speed statistics to the server after a successful download
 * Fixed the GUI freeze when someone is queueing a lot of files
 * "Download containing folder" was not working in all cases
 * Reduced rescan time
 * Added /rsearch, /bsearch, /usearch
 * Status bar now shows the number of users downloading/uploading
 * /unban was not working


## Version 1.0.3 (March 23, 2003)

 * Fixed a few bugs in the new shares rescanning code
 * Sorting transfers list sometimes caused a traceback


## Version 1.0.2 (March 21, 2003)

 * Configurable port range (patch from Hyriand)
 * Room and userlist searches (based on patch from Hyriand)
 * Online/Away/Offline status in the statusbar (patch from Hyriand)


## Version 1.0.1 (March 20, 2003)

 * Rescanning of shares now skips over directories that have not changed
   (inspired by hyriand's patch)
 * It is possible to optionally rescan shares on startup
 * Rescanning of shares now does not freeze the GUI


## Version 1.0.0 (March 12, 2003)

 * Fixes for possible temporary UI freezes
 * Removed "user phrases turn grey" feature, because it triggers gtk bug
   causing a segfault
 * Fixed a problem with clearing transfers
 * Rescanning of shares wasn't possible under gtk2
 * If we send search results to someone this is now always displayed in the
   log window
 * Fixes for "Download containing folder"
 * Added missing menu entries to search tabs, filelist tabs and userlists
 * It is now possible to refresh the filelist of the other user
 * Buttons on the user-info rearranged and some new added
 * Show ip address now does reverse DNS lookup
 * Unrecognized commands in chat are no longer sent as chat phrases


## Version 1.0.0pre6 (March 10, 2003)

 * Added script for importing configuration from the windows version
   (provided by geertk)
 * It is now possible to change the path for writing log files
 * Bogus config sections no longer cause a traceback
 * pyslsk now resumes files left over by the official windows client
 * phrases said by users no longer present in the room turn grey now
 * wxPython 2.4.0.4 is now supported
 * Sorting is now case-insensitive


## Version 1.0.0pre5a (March 2, 2003)

 * Fixed a silly bug with searching


## Version 1.0.0pre5 (March 2, 2003)

 * Banning (patch from Hyriand)
 * Upload bandwidth management (patch from Hyriand)
 * Numbers are now formatted according to locale rules
 * Total upload and download bandwidth usage is shown in the status bar
 * Various / commands in chat (see Help menu for full description)
   (patch from Hyriand)
 * Nickname completion in chat (patch from Hyriand)


## Version 1.0.0pre4 (February 28, 2003)

 * Config files are now saved every time a configurration is changed, not
   just on exit
 * Fixed a silly typo in FolderContentsResponse
 * Fix against potential distributed network attack
 * Fix for Unicode support in settings window


## Version 1.0.0pre3 (February 26, 2003)

 * Fixed handling of "Download containing folder" requests from other peers
 * Fixed stuck "Establishing connection"
 * Administrative messages are now supported
 * Fixes for distributed network support
 * Hopefully fixed the exit problem (where pyslsk waits for a while and
   then prints a bunch of tracebacks)
 * Fixed a DoS vulnerability found by hyriand


## Version 1.0.0pre2 (February 23, 2003)

 * Fixes for bugs in 1.0.0pre1
 * "Download containing folder" should now be possible for search
   results that pyslsk returns


## Version 1.0.0pre1 (February 22, 2003)

 * Pysoulseek is now searchable; it does not however support being a parent node
   in the distributed network
 * Unicode support that allows using pyslsk with Unicode builds of wxPython,
   such as Gtk2 build
 * Reduced flicker in transfers panels
 * Reduced CPU/memory consumption when uploading big files
 * Shared files database is now stored in a pickled format in a separate file
   \<config\>.shares
 * Fixed a problem with broken VBR mp3 files
 * A situation when someone else logs in under our nickname is now handled
   gracefully
 * pyslsk now responds to place in queue requests
 * It is now possible to exit pyslsk when a server connection is in progress
 * Download directory is now created when the transfer starts
 * Inverse colour gtk themes are now usable with pyslsk
 * A bunch of smaller bugfixes


## Version 0.4.11 (January 15, 2003)

 * wxPython 2.3.4 at least is now required as the previous versions had trouble
   displaying user info picture
 * Chatrooms and private chat conversations can now be written to files
   (patch by Zip)
 * Fixed a problem with transfers stuck in "Waiting for peer to connect"
 * Fixed a problem with changes in userlist or the whole userlist being
   lost sometimes
 * Fixed potential problems with asynchronous connect()
 * Empty files are now uploaded and downloaded correctly
 * Fixed a problem with scanning unreadable directories
 * It is now possible to exit during the auto-reconnect
 * pyslsk was autoreconnecting when the server did not let us in due
   to the wrong password or other valid reason
 * Away state is now preserved during the reconnect


## Version 0.4.10d (January 2, 2003)

 * ID3 mp3s are now scanned quicker
 * Retrying aborted transfers if the user has logged off is now handled
   correctly
 * If a transfer is negotiated and new transfer requests arrive, they are
   queued
 * Disconnecting now correctly handles changes in downloads and user list
 * Clicking on column header outside the titles no longer produces a traceback


## Version 0.4.10c (December 31, 2002)

 * Fixed a few tracebacks
 * wxPython 2.3.3 has a problem with displaying user info, so 2.3.4 is
   now required


## Version 0.4.10b (December 25, 2002)

 * Backed out the 0.4.10a fix, as it does not fix every case; you have to
   rescan the shared folders through the settings window to upgrade properly
 * Added a postcards statement


## Version 0.4.10a (December 24, 2002)

 * Fixed a problem with upgrading shared files list to the new format


## Version 0.4.10 (December 23, 2002)

Christmas release

 * pyslsk now tries to reuse the same address when opening a listening socket
   (patch from waxed)
 * Bitrate and length of VBR mp3s are now correctly determined
 * Length and bitrate of shared Ogg Vorbis files are now determined,
   if Python Vorbis bindings are installed
 * Updated subtabs are now marked with icons, like the main tabs.
 * It is possible to close/open rooms list, like the user list
 * Further reduced the CPU usage during sending the list of shared files
   to other peers
 * Added "Close and ignore" button to search tabs (it closes a search tab and
   discards further search results)
 * Updated Mac OS X instructions
 * pyslsk now uses commandline switches: --help for help, -c for an alternative
   config file
 * pyslsk now correctly shutdowns on SIGTERM
 * "Waiting for peer to connect" states now timeout after 5 minutes to "Cannot
   connect" state (untested)
 * pyslsk now tries to reconnect to a server if the server closes the
   connection
 * a problem with dynamic ip addresses was fixed
 * pyslsk now locks files when writing to them
 * colours in chat: blue for own phrases, green for /me things, black
   for everything else
 * picture in user info tab can be scrolled now


## Version 0.4.9b (November 24, 2002)

 * Fixed an obscure problem with reading config files
 * It's now again possible to save users' pictures


## Version 0.4.9a (November 23, 2002)

 * The number of the shared files is now updated on the server after a rescan
   of the shared folders
 * Increased the default width of the directory column in the Search tab
 * wxWindows is not actually required, only wxPython
 * Not all debug messages were filtered out
 * Away/returned/joined/left messages are now only displayed once


## Version 0.4.9 (November 22, 2002)

 * Errors in the config file are not anymore silently ignored
 * It is now possible to switch off debug messages in the log window
 * The number of the shared files is now updated on the server after each
   successful download
 * The main window resize is now handled correctly
 * Significantly reduced CPU usage during transfers, and during sending
   the list of shared files to other peers
 * A few cosmetic fixes


## Version 0.4.8 (November 9, 2002)

 * Binary RPM is now provided
 * Added RPM building tips to the installation instrictions
 * It is now possible to join selected rooms automatically on startup
 * If possible, the client connects automatically on startup
 * User's status is now shown in private chat window
 * It is now possible to toggle status between Online and Away
 * A bug that caused some uploads to fail is fixed
 * Added "Leave" button to the chatroom window


## Version 0.4.7 (October 26, 2002)

 * Added User List (Buddy List) capability
 * Fixed a few potential tracebacks
 * A correct response to a queue request that cannot be served is now given
 * Newly created subfolders in download folder were not added to shared list
 * Updated Mac OS X instructions
 * It is now possible to download all selected files and not just the
   focused one


## Version 0.4.6b (October 12, 2002)

 * It was not possible to create a configuration from scratch (new users)


## Version 0.4.6a (October 12, 2002)

 * It was necessary to provide a picture in order to connect
 * Self-description was corrupted each time the settings window was reopened


## Version 0.4.6 (October 11, 2002)

Dedicated to the memory of my father.

 * All lists are now sortable
 * Fixed a problem with non-blocking sockets on FreeBSD
 * Fixed a possible crash when closing a socket
 * Fixed a few potential transfer problems
 * Fixed a few GUI problems with wxPython 2.3.3; this version is now
   required
 * It is now possible to save pictures from users' information.
 * Added locale-aware timestamps in chat
 * Optional sharing of download folder is now possible
 * It is now possible to provide personal information (description and
   picture) to others


## Version 0.4.5 (September 12, 2002)

 * Removed the Global Users List function, because the server no longer
   supports it
 * "Uploads are stuck in the queued state forever" problem should now really
   be gone
 * Idle peer connections are now closed after a timeout of two minutes
 * The client no longer crashes if it reaches a limit of open sockets or files
 * Fixed a problem with duplicate upload requests (the second one has no effect
   now)
 * Ogg Vorbis files are now uploaded before any other files (but after files
   requested by privileged users)
 * Fixed a problem with accelerator keys
 * The search results tabs now open immediately after the search request
   is made
 * It is now possible to send private messages from the transfers window
 * Retrying uploads now has no effect
 * If an upload is aborted or cleared, the upload queue is now checked
   for queued uploads that could be started


## Version 0.4.4 (August 27, 2002)

 * The situation when either the uploader or the downloader logs off or back on
   should be handled gracefully now
 * "Uploads are stuck in the queued state forever" and "The bandwidth
   limitation has no effect" problems should be gone
 * Fixed a problem with accelerator keys


## Version 0.4.3 (August 23, 2002)

 * When the uploaded file was not the last one in the upload queue, the upload
   went horribly wrong


## Version 0.4.2 (August 23, 2002)

 * Fixed a couple of locale problems
 * Fixed a problem with a notification of a download failure
 * It is now possible to get place in line for queued downloads


## Version 0.4.1 (August 21, 2002)

 * Fixed a bug where subsequent upload requests from the same user
   or notifications of a download failure caused a crash
 * Failed downloads are now retried if there's an explicit notification from
   the uploader
 * Reduced flicker in the transfers tabs
 * Binary RPM packages should now include GUI modules


## Version 0.4.0 (August 19, 2002)

 * Added files sharing and uploads
 * Updated OS X instructions
 * Renamed the main executable to pyslsk
 * Added download privileges checking
 * Fixed a bug where users with no locale setting were not able to chat
 * Added speed, time elapsed/left to transfers lists
 * Search results now show how much files users have in queue
 * Clearing transfers should now work correctly


## Version 0.3.4a (August 8, 2002)

 * Updated pyslsk to use the new server list location on slsk.org


## Version 0.3.4 (August 4, 2002)

 * Added Mac OS X instructions in README.OSX file
 * Reworked the INSTALL file somewhat
 * Added timestamps to private chat messages
 * Added network character encoding selection (users in Russia will greatly
   appreciate this)
 * Separated UI classes from high-level logic to allow for other UI frontends
   in the future
 * Added searching within a specific user's files and folders
 * Windows that have been updated but not yet switched into are now
   marked with an icon on the tab


## Version 0.3.3 (June 30, 2002)

 * The official client and server reverted back to the old protocol to
   save bandwidth, and so do we.


## Version 0.3.2 (June 15, 2002)

 * Added a few startup checks of the environment (libs versions etc.)
 * Transfer requests now go through the same connection
 * Queued transfers now work again


## Version 0.3.1 (June 7, 2002)

 * A few crashes have been fixed
 * Yet another protocol tweak has been implemented (on login the client
   sends its version to the server, as pyslsk version numbers have no relation to
   official client versions, we send a bogus high number).


## Version 0.3.0 (May 27, 2002)

 * The new backwards-incompatible (but nuch better) file transfer
   protocol is now supported
 * Changes in peer-to-peer protocol are now supported


## Version 0.2.0 (April 28, 2002)

 * The new backwards-incompatible protocol introduced in v117
   of the official client is now supported.
 * Added multiple chatrooms capability.
 * Added global users list window.


## Version 0.1.1 (April 3, 2002)

 * Fixed an embarrassing bug where clicking OK in settings window did
   not actually change the settings
 * Active transfers are now correctly saved and resumed


## Version 0.1.0 (March 31, 2002)

 * Online/away status is now shown in users list
 * Added About dialog box
 * Added the list of official servers to choose from, taken from official
   website
 * Added downloads. Remotely queued downloads, 'Download folder' in user
   browse window, 'Download containing folder' in search result window,
   saving/restoring download list on exit/startup are all supported.


## Version 0.0.0 (February 10, 2002)

  * Initial release. Supports public chat, private chat, file searches,
    filelists browsing, users info browsing.
