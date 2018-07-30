# vim: set fileencoding=utf-8 :
from StringIO import StringIO
import commands
import json


# あいうえお
def main():
    #    a = commands.getoutput("curl -XGET https://www.google.com/")
    #    b = StringIO(a).read()
    #    print(b)
    c = json.load(open("hgoe.json"))
    for ele in c["service_catalog"]:  # たかだか1,2個
        if ele['type'] == 'volumev2':
            ele["endpoints"][0]['internalURL'] = ele["endpoints"][0]['internalURL'].replace(c["project_id"],"aaaaaaaaaaaaaaaaaaaa")

    print(c["service_catalog"])


if __name__ == '__main__':
    main()
