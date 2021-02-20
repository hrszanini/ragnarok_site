import fastapi
import services
import controllers


def configure_page_routes(app: fastapi.FastAPI):
    @app.get('/')
    def home_page():
        return html_file('index.html')

    @app.get('/favicon.ico')
    def favicon():
        fav_file_path = '{}/favicon.ico'.format(services.RESOURCES_PATH)
        return fastapi.responses.FileResponse(fav_file_path, media_type='img/ico')

    @app.get('/{file}')
    def html_file(file: str):
        html_file_path = '{}/html/{}'.format(services.RESOURCES_PATH, file)
        return fastapi.responses.HTMLResponse(open(html_file_path, 'r', encoding='utf8').read())

    @app.get('/css/{file}')
    def css_file(file: str):
        css_file_path = '{}/css/{}'.format(services.RESOURCES_PATH, file)
        return fastapi.responses.HTMLResponse(open(css_file_path, 'r', encoding='utf8').read())

    @app.get('/js/{file}')
    def css_file(file: str):
        js_file_path = '{}/js/{}'.format(services.RESOURCES_PATH, file)
        return fastapi.responses.HTMLResponse(open(js_file_path, 'r', encoding='utf8').read())

    @app.get('/img/{file}')
    def css_file(file: str):
        img_file_path = '{}/img/{}'.format(services.RESOURCES_PATH, file)
        return fastapi.responses.FileResponse(img_file_path, media_type='img/png')


def configure_api_routes(app: fastapi.FastAPI):
    @app.get('/api/check_user')
    def get_check_user(user_id: str):
        return services.check_user(user_id)

    @app.post('/api/user')
    def post_add_user(new_user: controllers.NewUser):
        return services.insert_user(user_id=new_user.user_id,
                                    user_password=new_user.user_password,
                                    user_email=new_user.user_email,
                                    user_birthday=new_user.user_birthday)

    @app.get('/api/user')
    def get_user(user_id: str):
        return services.get_user(user_id).show()

    @app.put('/api/user/password')
    def put_update_password(login: controllers.Login):
        user = services.login(login.user_id, login.user_password)
        return services.update_password(user=user,
                                        new_password=login.new_password)


def configure_test_routes(app: fastapi.FastAPI):
    @app.get('/test/user')
    def get_user(user_id: str):
        return services.get_user(user_id)
