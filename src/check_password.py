class Check_password:
    def __init__(self):
        pass

    def check_password(self, password):
        bad_combinations = "qwertyuiop asdfghjkl zxcvbnm йцукенгшщзхъ фывапролджэё ячсмитьбю 0123456789"
        for i in range(len(password) - 2):
            if password[i:i + 3].lower() in bad_combinations:
                return 'bad comb'
        if len(password) < 9:
            return 'wrong lengh'
        elif password.lower() == password or password.upper() == password:
            return "one registr"
        elif password.isdigit():
            return "even digits"
        return 'ok'
