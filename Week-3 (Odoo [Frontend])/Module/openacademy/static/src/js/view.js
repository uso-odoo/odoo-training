odoo.define('openacademy.view', function (require) {
    "use strict";

    var AbstractAction = require('web.AbstractAction');
    var Widget = require('web.Widget');
    var core = require('web.core');

    var  Action =  AbstractAction.extend({
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
            'click .add': '_add',
            'click .remove': '_remove',
            'click .delete': '_delete',
        },

        init: function () {
            this._super.apply(this, arguments);
            this.counter = 0;
        },

        _add: function (ev) {

            console.log('Button Clicked')
            this.counter++;
            
            debugger;
            
            var $tr = $('<tr>', {
/*                text: this.counter,*/
/*                class: "myTr",*/
            });
            
            var $td1 = $('<td>', {
                text: this.counter,
/*                class: "myTd",*/
            });

            var $td = $('<td><input type="text" value=""/>', {

/*                class: "myTd",*/
            });

            debugger;
            
            var $button = $('<i>',{
                class: 'fa fa-trash icon delete'
            });
            
            debugger;
            $td1.appendTo($tr)
            $td.appendTo($tr);
            
            $button.appendTo($tr);
            
            $tr.appendTo(this.$el.find('tbody'));
        },

        _remove: function (ev) {
            
            console.log('Button Clicked')

            this.$el.find('tbody tr:last').remove();    
            this.counter--;

        },

        _delete: function (ev) {

            console.log('Button Clicked')
            // delete row
            var $currentTableRow = this.$(ev.currentTarget).parents('tr');
            $currentTableRow.remove();
        },
    });

    core.action_registry.add('store', Action);
});



