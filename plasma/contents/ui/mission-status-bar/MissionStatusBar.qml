import QtQuick 2.15
import QtQuick.Layouts 1.15
import "../status-widgets"

Item {
    id: root

    width: 1920
    height: 30

    property string panelState: "STATE_UNKNOWN"
        property string currentWorkspace: "WORKSPACE UNKNOWN"

            readonly property var validPanelStates: [
                "STATE_UNKNOWN",
                "READY",
                "OPERATIONAL",
                "ATTENTION",
                "DEGRADED",
                "CRITICAL"
            ]

            readonly property color backgroundColor: "#161C22"
                readonly property color surfaceColor: "#1B232B"
                    readonly property color borderColor: "#2B3640"
                        readonly property color primaryText: "#D8DEE9"
                            readonly property color secondaryText: "#AAB4C0"

                                onPanelStateChanged: {
                                    if (validPanelStates.indexOf(panelState) === -1)
                                    {
                                        panelState = "CRITICAL"
                                    }
                                }

                                function railColor()
                                {
                                    switch (panelState) {
                                        case "STATE_UNKNOWN": return "#AAB4C0";
                                        case "READY": return "#00FF66";
                                        case "OPERATIONAL": return "#2F6B3F";
                                        case "ATTENTION": return "#FFD400";
                                        case "DEGRADED": return "#FF7A33";
                                        case "CRITICAL": return "#FF3030";
                                        default: return "#FF3030";
                                    }
                                }

                                Rectangle {
                                    anchors.fill: parent
                                    color: root.backgroundColor
                                }

                                Rectangle {
                                    id: identityZone
                                    x: 0
                                    y: 0
                                    width: 96
                                    height: 26
                                    color: root.surfaceColor
                                    border.color: root.borderColor
                                    border.width: 1

                                    Text {
                                        anchors.centerIn: parent
                                        text: "CC-01"
                                        color: root.primaryText
                                        font.pixelSize: 11
                                        font.bold: true
                                    }
                                }

                                Rectangle {
                                    id: workspaceZone
                                    x: 96
                                    y: 0
                                    width: parent.width - 96 - 360
                                    height: 26
                                    color: root.backgroundColor
                                    border.color: root.borderColor
                                    border.width: 1

                                    Text {
                                        anchors.verticalCenter: parent.verticalCenter
                                        anchors.left: parent.left
                                        anchors.leftMargin: 16
                                        text: root.currentWorkspace
                                        color: root.primaryText
                                        font.pixelSize: 11
                                        font.bold: true
                                    }

                                    Text {
                                        anchors.verticalCenter: parent.verticalCenter
                                        anchors.right: parent.right
                                        anchors.rightMargin: 16
                                        text: root.panelState
                                        color: root.secondaryText
                                        font.pixelSize: 10
                                    }
                                }

                                Rectangle {
                                    id: statusZone
                                    x: parent.width - 360
                                    y: 0
                                    width: 360
                                    height: 26
                                    color: root.surfaceColor
                                    border.color: root.borderColor
                                    border.width: 1

                                    Row {
                                        id: statusWidgetHost
                                        anchors.verticalCenter: parent.verticalCenter
                                        anchors.left: parent.left
                                        anchors.leftMargin: 16
                                        spacing: 18


                                        AudioWidget {
                                        }
                                        VpnWidget {
                                        }
                                        WifiWidget {
                                        }
                                        BluetoothWidget {
                                        }
                                        ClockWidget {
                                        }
                                        BatteryWidget {
                                        }
                                        PowerWidget {
                                        }





                                    }
                                }

                                Rectangle {
                                    id: statusRail
                                    anchors.left: parent.left
                                    anchors.right: parent.right
                                    anchors.bottom: parent.bottom
                                    height: 4
                                    color: root.railColor()
                                }
                            }