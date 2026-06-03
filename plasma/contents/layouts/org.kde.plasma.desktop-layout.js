var d = desktops();

var imgs = [
    "/home/authoritarian/Projects/CodexCommand/plasma/contents/wallpapers/Center_monitor_wallpaper.png",
    "/home/authoritarian/Projects/CodexCommand/plasma/contents/wallpapers/left_monitor_wall paper.png",
    "/home/authoritarian/Projects/CodexCommand/plasma/contents/wallpapers/right_monitor_wallpaper.png"
];

for (var i = 0; i < d.length && i < imgs.length; i++) {
    d[i].wallpaperPlugin = "org.kde.image";
    d[i].currentConfigGroup = ["Wallpaper", "org.kde.image", "General"];
    d[i].writeConfig("Image", "file://" + imgs[i]);
}
