import QtQuick 2.15
import QtQuick.Window 2.15

Window {
    id: testWindow

    width: 1920
    height: 30
    visible: true
    color: "#101418"
    title: "Codex Command Mission Status Bar Test"

    MissionStatusBar {
        anchors.fill: parent
        currentWorkspace: "WS-01 CODING"
    }
}
