def listinterface():

    import ifaddr

    adapters = ifaddr.get_adapters()
    interface = interface.encode('utf-8')
    for adapter in adapters:
        print("------------")
        print(adapter.name)
        print(adapter.ips)
        print("------------")
listinterface()
