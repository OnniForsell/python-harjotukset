vuodenajat = ("talvi", "talvi", "kevät", "kevät", "kevät", "kesä", "kesä", "kesä", "syksy", "syksy", "syksy", "talvi", )

while True:
    kk = int((input("Anna kuukausi numerona (1-12): "))) - 1
    print(f"{kk + 1} on {vuodenajat[kk]} kuukausi")
