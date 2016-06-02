module.exports = function(grunt) {
    'use strict';
    require('load-grunt-tasks')(grunt);

    /**
     * LocalConfig
     */
     var LocalConfig = {
        dev: "static",
        dist: "static",
        js: "assets/js",
        sass: "assets/scss",
        css: "stylesheets/",
        img: "assets/images",
        font: "assets/fonts",
        icon: "assets/svg-icons",
        convert: "assets/convert"
    };
    /**
     * bowerPath
     */
     var bowerPath = {
        root_path: './static/bower_components',
        bootstrap: '<%= bowerPath.root_path %>/bootstrap-sass/assets',
        fontawesome: '<%= bowerPath.root_path %>/font-awesome-sass/assets',
        flexslider: '<%= bowerPath.root_path %>/flexslider',
        jquery: '<%= bowerPath.root_path %>/jquery',
    }

    /**
     * Init Config
     */
     grunt.initConfig({
        pkg: grunt.file.readJSON("package.json"),
        config: LocalConfig,
        bowerPath: bowerPath,
        /**
         * meta
         */
         meta: {
            banner_dev: '/*\n' +
            'Theme Name: <%= pkg.title %> Dev\n' +
            'Theme URI: <%= pkg.url %>\n' +
            'Description: <%= pkg.title %> Develop\n' +
            'Version: <%= pkg.version %>\n' +
            'Author: <%= pkg.author.name %>\n' +
            'Author URI: <%= pkg.author.url %>\n' +
            '*/\n',
            banner: '/*\n' +
            'Theme Name: <%= pkg.title %> Production\n' +
            'Theme URI: <%= pkg.url %>\n' +
            'Description: <%= pkg.title %> Production\n' +
            'Version: <%= pkg.version %>\n' +
            'Author: <%= pkg.author.name %>\n' +
            'Author URI: <%= pkg.author.url %>\n' +
            '*/\n',
        },
        /**
         * clean
         */
         clean: {
            dist: {
                options: { force: true },
                src: ["<%= config.dist %>"]
            },
            css: {
                options: { force: true },
                src: ["<%= config.dev %>/<%= config.css %>/*.css"]
            },
            tmp: {
                options: { force: true },
                src: ["<%= config.dev %>/.tmp"]
            },
            sass_cache: {
                options: { force: true },
                src: [".sass-cache"]
            },
            jquery: {
                options: { force: true },
                src: ["<%= config.dev %>/<%= config.js %>/vendor/jquery.min.js", '<%= config.dev %>/<%= config.js %>/vendor/jquery.min.map']
            },
            favicons: {
                options: { force: true },
                src: [
                "<%= config.dev %>/<%= config.img %>/favicons/"
                ]
            },
            webfont_before_build: {
                options: { force: true },
                src: ["<%= config.dev %>/<%= config.icon %>/svg/*.svg"]
            },
            webfont_build: {
                options: { force: true },
                src: ["<%= config.dev %>/<%= config.icon %>/*.svg"]
            },
            convert_less: {
                options: { force: true },
                src: [
                "<%= config.dev %>/<%= config.convert %>/less/scss/**"
                ]
            },
            convert_css: {
                options: { force: true },
                src: [
                "<%= config.dev %>/<%= config.convert %>/css/scss/*"
                ]
            }
        },

        /**
         * lessToSass
         */
         lessToSass: {
            dev: {
                files: [{
                    expand: true,
                    cwd: '<%= config.dev %>/<%= config.convert %>/less',
                    src: ['*.less'],
                    ext: '.scss',
                    dest: '<%= config.dev %>/<%= config.convert %>/less/scss/',
                    rename: function(dest, src) {
                        return dest + src.replace('', '_');
                    }
                }],
                options:
                {
                    replacements: [{
                        pattern: /(\s+)\.([\w\-]*)\s*\((.*)\);/gi,
                        replacement: '$1@include $2($3)',
                        order: 2
                    }]
                }
            },
        },
        /**
         * sass-convert
         */
         'sass-convert': {
            options: {
              from: 'css',
              to: 'scss',

            },
            files: {
                cwd: '<%= config.dev %>/<%= config.convert %>/css',
                src: ['*.css'],
                filePrefix: '_',
                dest: '<%= config.dev %>/<%= config.convert %>/css/scss'
            }
        },


        /**
         * concat
         */
         concat: {
            options: {
                separator: ';'
            },
            js: {
                src: ['<%= config.dev %>/<%= config.js %>/main.js'],
                dest: '<%= config.dev %>/.tmp/<%= config.js %>/final.js'
            },
            libs: {
                src: ['<%= config.dev %>/<%= config.js %>/libs/*.js'],
                dest: '<%= config.dev %>/.tmp/<%= config.js %>/libs_final.js'
            },
            css: {
                src: ['<%= config.dev %>/<%= config.sass %>/**/*.css'],
                dest: '<%= config.dev %>/.tmp/final.css'
            },
        },
        /**
         * uglify
         */
         uglify: {
            options: {
                mangle: true,
                banner: "<%= meta.banner %>"
            },
            dev: {
                files: {
                    "<%= config.dev %>/<%= config.js %>/main.min.js": ["<%= concat.js.dest %>"],
                    "<%= config.dev %>/<%= config.js %>/libs.min.js": [
                    "<%= concat.libs.dest %>"
                    ]
                }
            },
            dist: {
                files: {
                    "<%= config.dist %>/<%= config.js %>/main.min.js": ["<%= concat.js.dest %>"],
                    "<%= config.dist %>/<%= config.js %>/libs.min.js": [
                    "<%= concat.libs.dest %>"
                    ]
                }
            }
        },
        /**
         * copy
         */
         copy: {
            jquery: {
                files: [{
                    expand: true,
                    cwd: '<%= bowerPath.jquery %>/dist',
                    src: ['jquery.min.js', 'jquery.min.map'],
                    dest: '<%= config.dev %>/<%= config.js %>/vendor'
                }]
            },
            webfont_rename_svg: {
                files: [{
                    expand: true,
                    flatten: true,
                    cwd: '<%= config.dev %>/<%= config.icon %>/',
                    src: ['*.svg'],
                    dest: '<%= config.dev %>/<%= config.icon %>/svg/',
                    rename: function(dest, src) {
                        return dest + src.replace('muglabs_', '');
                    }
                }, ]
            },
            dist: {
                files: [{
                    expand: true,
                    dot: true,
                    cwd: '<%= config.dev %>/',
                    src: [
                    '**',
                    '*.{md,txt,htaccess}',
                    '!<%= config.images %>**/.{png,jpg,jpeg}',
                    '!_**/**',
                    '!**.{html}',
                    '<%= config.css %>/*.css',
                    '!<%= config.sass %>/**',
                    '!<%= config.icon %>/**',
                    '!<%= config.js %>/libs/**',
                    '<%= config.js %>/vendor/**',
                    '!.tmp/**',
                    '!./*.pot',
                    '!bower_components/**',
                    '!<%= config.convert %>/**',
                    '!<%= config.js %>/*.js'
                    ],
                    dest: '<%= config.dist %>/'
                }]
            }
        },
        /**
         * compass
         */
         compass: {
            dev: {
                options: {
                    force: true,
                    config: "config.rb",
                    outputStyle: "compressed",
                    sassDir: "<%= config.dev %>/<%= config.sass %>",
                    cssDir: "<%= config.dev %>/<%= config.css %>",
                    banner: "<%= meta.banner %>",
                    specify: "<%= config.dev %>/<%= config.sass %>/*.scss",
                    importPath: [
                    '<%= bowerPath.bootstrap %>/stylesheets/',
                    '<%= bowerPath.fontawesome %>/stylesheets/',
                    ]
                }
            },
            dist: {
                options: {
                    force: true,
                    config: "config.rb",
                    outputStyle: "compressed",
                    sassDir: "<%= config.dev %>/<%= config.sass %>",
                    cssDir: "<%= config.dev %>/<%= config.css %>",
                    banner: "<%= meta.banner %>",
                    specify: "<%= config.dev %>/<%= config.sass %>/*.scss",
                    importPath: [
                    '<%= bowerPath.bootstrap %>/stylesheets/',
                    '<%= bowerPath.fontawesome %>/stylesheets/',
                    ]
                }
            }
        },
        /**
         * csslint
         */
         csslint: {
            dev: {
                csslintrc: '.csslintrc'
            },
            strict: {
                src: ['<%= config.dev %>/<%= config.css %>/*.css']
            }
        },

        /**
         * htmlmin
         */
         htmlmin: {
            dist: {
                options: {
                    removeComments: false,
                    collapseWhitespace: false
                },
                files: [{
                    expand: true,
                    cwd: '<%= config.dev %>/',
                    src: '*.{html,php}',
                    dest: '<%= config.dist %>/',
                }],
            }
        },
        /**
         * cssmin
         */
         cssmin: {
            options: {
                stripBanners: true,
                banner: "<%= meta.banner %>"
            },
            combine: {
                files: {
                    '<%= config.dev %>/<%= config.css %>/assets/css/libs.css': ['<%= concat.css.dest %>']
                }
            }
        },
        /**
         * jshint
         */
         jshint: {
            options: {
                jshintrc: ".jshintrc"
            },
            all: [
            "Gruntfile.js",
            "<%= config.dev %>/<%= config.js %>/main.js",
            "<%= config.dev %>/<%= config.js %>/libs/**"
            ]
        },
        /**
         * imagemin
         */
         imagemin: {
            dist: {
                options: {
                    optimizationLevel: 3,
                    cache: false
                },
                files: [{
                    expand: true,
                    cwd: '<%= config.dev %>/<%= config.images %>/',
                    src: ['**/*.{png,jpg,gif}'],
                    dest: '<%= config.dist %>/<%= config.images %>/',
                }],
            }
        },
        /**
         * rev
         */
         rev: {
            options: {
                algorithm: 'md5',
                length: 5
            },
            dist: {
                files: [{
                    src: [
                    '<%= config.dist %>/<%= config.images %>/**/*.{jpg,jpeg,gif,png}',
                    '<%= config.dist %>/<%= config.css %>/**/*.css',
                    '<%= config.dist %>/<%= config.js %>/**/*.js'
                    ]
                }]
            }
        },
        /**
         * useminPrepare
         */
         useminPrepare: {
            options: {
                dest: '<%= config.dist %>'
            },
            html: ['<%= config.dev %>/*.php', '<%= config.dev %>/*.html']
        },
        /**
         * usemin
         */
         usemin: {
            options: {
                config: ['<%= config.dist %>']
            },
        html: ['<%= config.dist %>/{,*/}*.php', '<%= config.dist %>/{,*/}*.html'],
    },
        /**
         * compress
         */
         compress: {
            dev: {
                options: {
                    archive: '_zips/site_dev.zip'
                },
                files: [
                { src: ['<%= config.dev %>/**'], filter: 'isFile' }
                ]
            },
            dist: {
                options: {
                    archive: '_zips/site_prod.zip'
                },
                files: [
                { src: ['<%= config.dist %>/**'], filter: 'isFile' },
                ]
            }
        },
        /**
         * notify
         */
         notify: {
            compass: {
                options: {
                    title: "SASS - <%= pkg.title %>",
                    message: "Compilado e minificado com sucesso!"
                },
            },
            js: {
                options: {
                    title: "Javascript - <%= pkg.title %>",
                    message: "Minificado e validado com sucesso!"
                }
            },
        },
        /**
         * favicons
         */
         favicons: {
            options: {
                trueColor: true,
                precomposed: true,
                appleTouchBackgroundColor: "#fff",
                coast: true,
                windowsTile: false,
                tileBlackWhite: true,
                tileColor: "auto",
                firefox: false,
                html: '<%= config.dev %>/<%= config.img %>/favicons/favicons-header.txt',
                HTMLPrefix: "<%= config.dev %>/<%= config.img %>/favicons/"
            },
            icons: {
                src: '<%= config.dev %>/<%= config.img %>/favicon.png',
                dest: '<%= config.dev %>/<%= config.img %>/favicons'
            },
        },
        /**
         * webfont
         */
         webfont: {
            icons: {
                src: '<%= config.dev %>/<%= config.icon %>/svg/*.svg',
                dest: '<%= config.dev %>/<%= config.font %>',
                destCss: '<%= config.dev %>/<%= config.sass %>/core/',
                options: {
                    hashes: false,
                    types: 'eot,woff,woff2,ttf,svg',
                    htmlDemo: false,
                    styles: 'icon',
                    embed: true,
                    syntax: 'bem',
                    stylesheet: 'scss',
                    relativeFontPath: '<%= config.font %>',
                    templateOptions: {
                        baseClass: 'mug',
                        classPrefix: 'mug-',
                        mixinPrefix: 'mug-'
                    }
                },
                destHtml: '<%= config.dev %>/<%= config.icon %>',
            }
        },

        /**
         * watch
         */
         watch: {
            options: {
                livereload: {
                    host: 'localhost',
                    port: 9000,
                }
            },
            csss_libs: {
                files: ["<%= config.dev %>/<%= config.scss %>/libs/*.css"],
                tasks: ["concat:css", "cssmin"]
            },
            css: {
                files: ["<%= config.dev %>/<%= config.sass %>/**/*.{scss,sass}"],
                tasks: ["clean:css", "compass:dev", "notify:compass"]
            },
            js: {
                files: ["<%= jshint.all %>"],
                tasks: ["concat", "uglify:dev", "notify:js"]
            },
            html: {
                files: [
                "/*.{html,htm,shtml,shtm,xhtml,php,jsp,asp,aspx,erb,ctp}"
                ]
            }
        },

    });

grunt.registerTask('w', ['watch']);
grunt.registerTask('prod', ['clean:dist', 'concat', 'cssmin', 'compass:dist', 'uglify:dist', 'copy:dist', 'imagemin:dist', 'useminPrepare', 'usemin']);
grunt.registerTask('jquery', ['clean:jquery', 'copy:jquery']);
grunt.registerTask('cache', ['rev', 'useminPrepare', 'usemin']);
grunt.registerTask('zip', ['compress:dist', 'compress:dev']);
grunt.registerTask('favicon', ['clean:favicons', 'favicons']);
grunt.registerTask('convert_less', ['clean:convert_less', 'lessToSass:dev']);
grunt.registerTask('convert_css', ['clean:convert_css', 'sass-convert']);

grunt.registerTask('icon', ['clean:webfont_before_build', 'copy:webfont_rename_svg', 'clean:webfont_build', 'webfont']);

};
