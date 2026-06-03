import QtQuick 2.15

Item {
    id: root

    width: 24
    height: 26

    property string widgetId: "clock"
        property string iconName: "clock"
            property bool widgetEnabled: true
                property int widgetPriority: 50

                    Rectangle {
                        anchors.centerIn: parent
                        width: 14
                        height: 14
                        color: "#FFD400"
                    }
                }