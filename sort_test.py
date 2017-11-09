if __name__ == '__main__':
    ss=["2017-08-02 14:26", "2017-07-19 14:59","2017-12-19 15:01:22", "2017-07-06 11:36","2017-07-19 15:02"]

    print ss

    ss = sorted(ss)

    print ss

    dd = {"list":[
        {"names":[

        ]}
    ]}

    print dd

    for item in dd.get("list",[]):
        lists = item.get("names",[])
        lists.append({"ss":"adad"})
        print lists


    print dd


