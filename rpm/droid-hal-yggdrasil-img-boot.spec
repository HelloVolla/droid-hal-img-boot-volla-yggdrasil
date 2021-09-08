%define device yggdrasil

%define mkbootimg_cmd mkbootimg --cmdline 'bootopt=64S3,32N2,64N2 loop.max_part=7 androidboot.selinux=permissive audit=0' --kernel %{kernel} --ramdisk %{initrd} --base 0x00000000 --pagesize 2048 --kernel_offset 0x40080000 --ramdisk_offset 0x55000000 --second_offset 0x40f00000 --tags_offset 0x54000000 --board '' --output

%define root_part_label userdata

%define display_brightness_path /sys/class/leds/lcd-backlight/max_brightness
%define display_brightness 255

%include initrd/droid-hal-device-img-boot.inc

