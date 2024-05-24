from src.models.user import User


def validate_registration(args):
    check_email = User.query.filter(User.email == args['email']).one_or_none()
    check_username = User.query.filter(User.username == args['username']).one_or_none()

    if check_username != None:
        return {'msg':'username already exist', 'is_validated': False}
    elif check_email != None:
        return {'msg':'email already exist', 'is_validated': False}
    else:
        return {'msg':'email already exist', 'is_validated': True}
    

    