.SUFFIXES:
.PHONY: all clean

MAKEFLAGS += -r
VPATH := template css src

dest := assets
css.dest := $(addprefix $(dest)/, $(wildcard css/*.css))
html.src := $(wildcard template/*.html)

js.src := $(wildcard src/*.js)
js.src += $(wildcard src/*/*.js)
js.dest := $(patsubst src/%, $(dest)/js/%, $(js.src))

all: $(dest)/pg.html $(dest)/css/atomic.css $(dest)/js/main.min.js $(css.dest)

clean:
	rm -rf $(dest)

$(dest) $(dest)/css $(dest)/js $(dest)/js/controllers:
	mkdir -p $@

$(dest)/%.html: %.html widget.html playground.py | $(dest)
	./playground.py $(patsubst template/%.html,%.html,$<) > $@.tmp
	mv $@.tmp $@

$(dest)/css/atomic.css: config.js $(html.src) node_modules/latest | $(dest)/css
	./node_modules/.bin/atomizer -c config.js -o $@ $(html.src)

$(dest)/css/%.css: %.css |$(dest)/css
	cp $< $@

$(dest)/js/%.js: %.js | $(dest)/js $(dest)/js/controllers
	./node_modules/.bin/babel --source-maps inline -o $@ $<

$(dest)/js/main.js: $(js.dest)
	./node_modules/.bin/browserify $(dest)/js/app.js -o $@ --debug

$(dest)/js/main.min.js: $(dest)/js/main.js
	./node_modules/.bin/uglifyjs $< -c -m --source-map includeSources,content=inline,url=main.min.js.map -o $@

node_modules/latest: package.json
	yarn install
	touch $@
