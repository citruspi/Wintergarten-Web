App.SearchController = Ember.Controller.extend({
    actions: {
        search: function () {
            this.transitionToRoute('/search/' + this.get('query'));
        }
    }
});
