
from db import fetch, insert;
from spotify_data import create_urilist

key_date = "Done for  2011-06-12"

def sum(*args):
    if len(args) != 0:
        total = 0
        for ar in args:
            total = total + ar;
        return total
    elif len(args) == 1:
        return args
    else:
        return 5;


if __name__ == "__main__":
    token = "BQCL8jhQqBSLF3mXCHdQcetVuTmWAE9D4EMA9YLO73DF0Cm16Vg-7GPvSzgGBvKoV8_nhv6GW-7rb8u6OktG5-TUITe3o9u7vfUbukJMB8TWjNPHjU1QoQP4yU0dLGhQN9d0jRi3rNtzKMqgijZ3RhGA0re4VPnsWUIwJuPxIuQiQPJrRs7peogaQwSRVQBawOP1Hb1LYO6K4Z2_cib2E1J1ZJXxA6yzTSSgz_4"
    songlist = fetch()
    urilist = create_urilist(token, songlist, 2)
    print(len(urilist))