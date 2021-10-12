%define device yggdrasil
%define BOARD_PREBUILT_VBMETAIMAGE %{getenv:ANDROID_ROOT}/device/gigaset/mt6763-common/prebuilt/vbmeta.img
%define BOARD_BOOTIMAGE_PARTITION_SIZE 33554432
%define INTERNAL_AVB_BOOT_SIGNING_ARGS %{nil}
%define BOARD_AVB_BOOT_ADD_HASH_FOOTER_ARGS %{nil}

%define mkbootimg_cmd mkbootimg --cmdline 'bootopt=64S3,32N2,64N2 loop.max_part=7 androidboot.selinux=permissive audit=0' --kernel %{kernel} --ramdisk %{initrd} --base 0x00000000 --pagesize 2048 --kernel_offset 0x40080000 --ramdisk_offset 0x55000000 --second_offset 0x40f00000 --tags_offset 0x54000000 --board '' --output

%define avbtool_footer_cmd avbtool add_hash_footer --partition_size %{BOARD_BOOTIMAGE_PARTITION_SIZE} --partition_name boot %(INTERNAL_AVB_BOOT_SIGNING_ARGS) %(BOARD_AVB_BOOT_ADD_HASH_FOOTER_ARGS) --image
%define avbtool_append_cmd avbtool append_vbmeta_image --partition_size %{BOARD_BOOTIMAGE_PARTITION_SIZE} --vbmeta_image %{BOARD_PREBUILT_VBMETAIMAGE} --image

%define root_part_label userdata

%define display_brightness_path /sys/class/leds/lcd-backlight/max_brightness
%define display_brightness 255

%include initrd/droid-hal-device-img-boot.inc

