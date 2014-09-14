App.SearchView = Ember.View.extend({
    didInsertElement : function(){
        this._super();
        Ember.run.scheduleOnce('afterRender', this, function(){

            function positionSearchField(){

                windowHeight = $(window).height();
                searchFieldHeight = $("#search-field").height();
                searchFieldMargin = (windowHeight - searchFieldHeight)/2;

                $('#search-field').css('margin-top', searchFieldMargin+'px');

            }

            window.onresize = function(event) {
                positionSearchField();
            };

            positionSearchField();

            $('#search-field').focus();

        });
    }
});
