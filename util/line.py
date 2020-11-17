import requests


class LINE():
    def lineNotifyMessage(self, msg):
        token = "qTGNw0nozeEA190TfCCyVm138RKldCLxE6ZCSwNwUd4"
        headers = {
            "Authorization": "Bearer " + token,
            "Content-Type": "application/x-www-form-urlencoded"
        }

        payload = {'message': msg}
        r = requests.post("https://notify-api.line.me/api/notify",
                          headers=headers,
                          params=payload)
        return r.status_code
