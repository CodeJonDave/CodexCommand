import QtQuick 2.15

Item {
    id: root

    width: 24
    height: 26

    property string widgetId: "wifi"
        property string iconName: "wifi"
            property bool widgetEnabled: true
                property int widgetPriority: 30

                    Rectangle {
                        anchors.centerIn: parent
                        width: 14
                        height: 14
                        color: "#00A3FF"
                    }
                }