from odoo import http

class Academy(http.Controller):
    @http.route('/academy/academy/', auth='public', website=True)
    def index(self, **kw):
        Teachers = http.request.env['academy.teachers']
        return http.request.render('openacademy.index', {
            'teachers': Teachers.search([])
        })

    # @http.route('/academy/<int:id>/', auth='public', website=True)
    # def teacher(self, id):
    #     return '<h1>{} ({})</h1>'.format(id, type(id).__name__)

    @http.route('/academy/<model("academy.teachers"):teacher>/', auth='public', website=True)
    def teacher(self, teacher):
        return http.request.render('openacademy.biography', {
            'person': teacher
        })





#    
# access_academy_teachers,access_academy_teachers,model_academy_teachers,,1,1,1,0
# access_manager,openacademy.course.manager,model_openacademy_course,openacademy.group_openacademy_manager,1,1,1,1
# access_user,openacademy.course.manager,model_openacademy_course,openacademy.group_openacademy_user,1,1,0,0
# access_manager_s,openacademy.course.manager,model_openacademy_session,openacademy.group_openacademy_manager,1,1,1,1
# access_user_s,openacademy.course.manager,model_openacademy_session,openacademy.group_openacademy_user,1,1,0,0





