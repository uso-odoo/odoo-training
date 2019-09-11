odoo.define('openacademy.view', function (require) {
    "use strict";

    var AbstractAction = require('web.AbstractAction');
    var Widget = require('web.Widget');
    var core = require('web.core');

    var  Demo =  AbstractAction.extend({
        template: 'page_html',
        xmlDependencies: ['/openacademy/static/src/xml/quiz_template.xml'],

        start: function () {
            this._super.apply(this, arguments);
            var createWid = new NewWidget();
            createWid.appendTo(this.$el);
        },

    });

    var NewWidget = Widget.extend({
        template: 'header_html',
        xmlDependencies: ['/openacademy/static/src/xml/quiz_template.xml'],

/*        function GetTodayDate() {
            var tdate = new Date();
            var dd = tdate.getDate(); //yields day
            var MM = tdate.getMonth(); //yields month
            var yyyy = tdate.getFullYear(); //yields year
            var currentDate= dd + "-" +( MM+1) + "-" + yyyy;

        return currentDate;
}
*/
        events: {
            'date': '_onDate',
        },
        
        _onDate: function (ev) {

            console.log('Date')
            
            debugger;
            
            var $tdate = new Date();

            var $dd = tdate.getDate(); //yields day

            var $MM = tdate.getMonth(); //yields month

            var $yyyy = tdate.getFullYear(); //yields year

            var $currentDate = dd + "-" + ( MM+1) + "-" + yyyy;

            $currentDate.appendTo(this.$el.find('.c_date'));
            
        },


    });

    core.action_registry.add('student', Demo);
});



