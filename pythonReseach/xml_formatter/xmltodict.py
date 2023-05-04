import json
import xmlto0dict


a = xmltodict.parser("\
<?xml version='1.0' encoding='UTF-8'?>\
    <sale>\
        <product>\
            <name> Product One </name>\
            <id> Product One </id>\
            <gova> Product One </gova>\
        </product>\
        <product>\
            <name> Product two </name>\
            <id> Product two</id>\
            <gova> Product two </gova>\
        </product>\
    </sale>"\
)

data = json.dumps(a)

print(a)
