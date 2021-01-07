import openclosed as open1
import openclosed_2 as open2
import openclosed_3 as open3

modules = [open1, open2, open3]

for module in modules:
    l1 = module.SystemMonitor({"before": {"session": 0}, "after": {"session": 1}})
    print(l1.identify_event().__class__.__name__)
    l2 = module.SystemMonitor({"before": {"session": 1}, "after": {"session": 0}})
    print(l2.identify_event().__class__.__name__)
    l3 = module.SystemMonitor({"before": {"session": 1}, "after": {"session": 1}})
    print(l3.identify_event().__class__.__name__)
    try:
        l4 = module.SystemMonitor({"after": {"transaction": "Tx001"}})
        print(l4.identify_event().__class__.__name__)
    except:
        pass
    print("Just tested the module: " + str(module))
