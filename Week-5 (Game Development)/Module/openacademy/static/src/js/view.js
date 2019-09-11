odoo.define('openacademy.view', function (require) {
    "use strict";

    var AbstractAction = require('web.AbstractAction');
    var Widget = require('web.Widget');
    var core = require('web.core');

    var  Demo =  AbstractAction.extend({
        template: 'simple_html',
        xmlDependencies: ['/openacademy/static/src/xml/view_js.xml'],

        start: function () {
            this._super.apply(this, arguments);
            var createWid = new NewWidget();
            createWid.appendTo(this.$el);
        },

    });

    var NewWidget = Widget.extend({
        template: 'widget_html',
        xmlDependencies: ['/openacademy/static/src/xml/view_js.xml'],

        events: {
            'click .add': '_onAdd',
            'click .delete': '_onDelete',
        },

        _onAdd: function (ev) {

            console.log('Button Clicked')
            
            debugger;
            
            var $tr = $('<tr>');
            
            var $td_name = $('<td><input type="text" name="username" />');

            var $td_gmail = $('<td><input type="text" name="gmail" />');
            
            var $td_phone = $('<td><input type="text" name="phone" />');

            debugger;
            
            var $button = $('<i>',{
                class: 'fa fa-trash mt-3 delete'
            });
            
            debugger;
            
            $td_name.appendTo($tr);
            $td_gmail.appendTo($tr);
            $td_phone.appendTo($tr);

            $button.appendTo($tr);
            
            $tr.appendTo(this.$el.find('tbody'));
        },

        _onDelete: function (ev) {

            console.log('Button Clicked')
            // delete row
            this.$(ev.currentTarget).parents('tr').remove();
        },
    });

    core.action_registry.add('store', Demo);
});



