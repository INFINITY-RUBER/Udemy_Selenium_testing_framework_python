# pip install psutil - pip install speedtest-cli
import psutil
import speedtest
from tabulate import tabulate


class Network_Detail(object):
    def __init__(self):
        self.parser = psutil.net_if_addrs()
        self.speed_parser = speedtest.Speedtest()
        # self.speed_parser.get_best_server()
        # self.speed_parser.download()
        # self.speed_parser.upload()
        self.interfaces = self.interface()[0]

    def interface(self):
        interfaces = []
        for interface_name, _ in self.parser.items():
            interfaces.append(str(interface_name))
        return interfaces
    
    def __repr__(self):
        down = str(f"{round(self.speed_parser.download() / 1_000_000, 2)}Mbps")
        up = str(f"{round(self.speed_parser.upload() / 1_000_000, 2)} Mbps")
        interface = self.interfaces
        data = {"interface:": [interface],
                "Download:": [down],
                "Upload:": [up]            
                }
        table = tabulate(data, headers="keys", tablefmt="pretty")
        return table

if __name__ == "__main__":
    print(Network_Detail())