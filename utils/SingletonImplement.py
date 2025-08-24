class SingletonImplement:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(SingletonImplement, cls).__new__(cls)
        return cls._instance