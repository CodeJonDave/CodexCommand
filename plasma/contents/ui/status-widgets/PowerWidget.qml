import QtQuick 2.15

Item {
    id: root

    width: 24
    height: 26

    property string widgetId: "power"
        property string iconName: "power"
            property bool widgetEnabled: true
                property int widgetPriority: 70

                    Rectangle {
                        anchors.centerIn: parent
                        width: 14
                        height: 14
                        color: "#FF3030"
                    }
                }