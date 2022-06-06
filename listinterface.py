def listinterface():

    import ifaddr

    adapters = ifaddr.get_adapters()
    for adapter in adapters:
        print("------------")
        print(adapter.name)
        print(adapter.ips)
        print("------------")
listinterface()
