build:

	bower install

	rm -rf static
	mkdir -p static/css
	mkdir -p static/js

	cp bower_components/bower-foundation/js/foundation.min.js static/js/foundation.min.js
	cp -r bower_components/bower-foundation/js/foundation static/js/foundation
	cp -r bower_components/bower-foundation/js/vendor static/js/vendor
	cp bower_components/moment/moment.js static/js/moment.min.js
	cp bower_components/backbone/backbone-min.js static/js/backbone.min.js
	cp bower_components/backbone/test/vendor/underscore.js static/js/underscore.js
	cp assets/wintergarten.js static/js/wintergarten.js

	cp bower_components/bower-foundation/css/normalize.css static/css/normalize.css
	cp bower_components/bower-foundation/css/foundation.min.css static/css/foundation.min.css
	cp assets/wintergarten.css static/css/wintergarten.css


