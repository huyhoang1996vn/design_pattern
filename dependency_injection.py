
class Config:
    def __init__(self) -> None:
        print("This is Config")
        


class Service:
    def __init__(self, config: Config) -> None:
        self.config = config    
        print("This is Service")



def main() -> None:
    config= Config()
    service = Service(config)  # <-- dependency


if __name__ == "__main__":
    main()