def add_user_query():
    return "insert into vpn_admin.usr(telegram_id, fullname, nickname) values (%s, %s, %s);"


def check_user_query():
    return "select count(1) from vpn_admin.usr where telegram_id=%s"


def add_user_token_outline_query():
    return "insert into vpn_admin.user_tokens(usr_id, usr_token) values (%s, %s);"


def set_disabled_token_query():
    return "update vpn_admin.user_tokens set enabled=false where guid=%s;"


def set_disabled_user_query():
    return "update vpn_admin.user_tokens set enabled=false where usr_id=%s;"
