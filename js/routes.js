App.ResultsRoute = Ember.Route.extend({
    model: function(params) {
        return Ember.$.getJSON('http://api.wintergarten.citruspi.io/films/search/'+params.query).then(function(data){
            data.results.forEach(function(result){
                result.poster_path = "https://image.tmdb.org/t/p/original" + result.poster_path;
                result.path = "/#/film/"+result.id;
            });
            return {
                'films': data.results,
                'query': params.query
            };
        });
    }
});

App.FilmRoute = Ember.Route.extend({
    model: function(params) {
        return Ember.$.getJSON('http://api.wintergarten.citruspi.io/films/title/'+params.id).then(function(data){
            return data;
        });
    }
});
