# Cyberduck

**Cyberduck** is a free graphical file manager for macOS and Windows. It lets you browse buckets, upload and download files with drag and drop.

## Installation

Download Cyberduck from [cyberduck.io](https://cyberduck.io/download/) and install it.

## Enable Path-Style Addressing

UzCloud Object Storage uses path-style addresses. Cyberduck has a separate connection profile for them:

1. Open **Preferences → Profiles** (on Windows: **Edit → Preferences → Profiles**).
2. Find **S3 (Deprecated path style requests)** and select the checkbox next to it.
3. Restart Cyberduck.

## Connect

1. Click **Open Connection**.
2. In the list of protocols, select **S3 (Deprecated path style requests)**.
3. **Server**: `s3.uzcstorage.uz`, **Port**: `443`.
4. Enter the **Access Key ID** and **Secret Access Key**.
5. Click **Connect**. The list of your buckets opens.

To save the connection for later, use **Bookmark → New Bookmark** with the same settings.

## Useful Features

- **Share** in the context menu of a file creates a temporary link (presigned URL).
- **Info** shows object metadata and lets you edit headers such as `Cache-Control`.

> [!TIP]
> **See also:**
>
> - **[Tools and connection parameters](overview.md)**
