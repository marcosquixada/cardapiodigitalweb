/**
 * IndexController
 * @namespace jaPedi.layout.controllers
 */
(function () {
  'use strict';

  angular
    .module('jaPedi.layout.controllers',['chart.js','ui.select2','highcharts-ng'])
    .config(['ChartJsProvider', function (ChartJsProvider) {
      // Configure all charts
      ChartJsProvider.setOptions({
        colours: ['#FF5252', '#FF8A80'],
        responsive: false
      });
      // Configure all line charts
      ChartJsProvider.setOptions('Line', {
        datasetFill: false
      });
    }])
    .config(['highchartsNGProvider', function (highchartsNGProvider) {
        Highcharts.setOptions({
           global: {
              useUTC: false,
            },
            lang: {
              decimalPoint: ',',
              thousandsSep: '.'
            },
           colors: ["#FFD700", "#afd8f8", "#cb4b4b", "#4da74d", "#9440ed", "#bd9b33", "#8cacc6"]
      });
    }])
    .controller('IndexController', IndexController);

  IndexController.$inject = ['$scope', '$route','UnidadesOrcamentarias', 'Orgaos','Localizacoes' ,'FontesRecurso','ProgramasTrabalho','Snackbar','$filter','$timeout','orderByFilter'];

  /**
   * @namespace IndexController
   */
  function IndexController($scope, $route, UnidadesOrcamentarias, Orgaos , Localizacoes, FontesRecurso, ProgramasTrabalho, Snackbar,$filter,$timeout, orderByFilter) {

    $scope.sections = [{title: "Home", slug: ""},
                        {title: "Sobre", slug: "sobre"},
                        {title: "Legislação", slug:"legislacao"},
                        {title: "Informativos", slug:"informativos"},
                        {title: "Ajuda", slug: "ajuda"},
                        {title: "Contato", slug: "contato"}];

    $scope.activeMenu = $scope.sections[0];

    $scope.selectedItem = null;
    $scope.selectedDate = 2016;
    $scope.selectedLocation = null;

    $scope.anos = [2014,2016]

    $scope.orgaoSelected = "";
    $scope.dsLocalizacaoSelected = "";

    $scope.vl_inicial_geral = 0.0;
    $scope.vl_atualizado_geral = 0.0;
    $scope.vl_empenhado_geral = 0.0;

    $scope.$watch(function() {
      if($route.current && $route.current.activetab){
          $scope.activeMenu = $route.current.activetab;
      }
       //return $route.current;
    },function(newValue,oldValue) {

    });

    $scope.tooltip_html = true;

    /*$scope.chart_1 = {
        labels : ["Janeiro","Fevereiro","Março"],
        series: ['Inicial','Atualizado','Empenhado'],
        data: []
    }*/

    /*$scope.chart_2 = {
        labels : [],
        series: ['Inicial','Atualizado','Empenhado'],
        data: []
    }*/


    $scope.chart_3 = {
        labels : [],
        data: []
    }


    $scope.chart_4 = {
        labels : [],
        series: ['Inicial','Atualizado','Empenhado'],
        data: []
    }

    $scope.chart_1 = {
        options: {
            chart: {
                type: 'column',
                inverted: false,
                options3d: {
                    enabled: true,
                    alpha: 0,
                    beta: 0,
                    depth: 20,
                    viewDistance: 25
                }
            },
            tooltip: {
              shared: true,
              valuePrefix: "R$ ",
              useHTML: $scope.tooltip_html
            },
          legend: {
            enabled: true
          }
        },
        xAxis: {
            categories: ["Janeiro","Fevereiro","Março"],
            title: {
                text: null
            }
        },
        yAxis: {
            min: 0,
            title: {
                text: 'Valor em R$',
                align: 'high'
            },
            labels: {
                overflow: 'justify'
            }
        },
        plotOptions: {
            bar: {
                dataLabels: {
                    enabled: true
                }
            }
        },
        series: [{
            name: "Inicial",
            data: []
        },{
            name: "Atualizado",
            data: []
        },{
            name: "Empenhado",
            data: []
        },],
        title: {
            text: ''
        },
        loading: false
    }



    $scope.chart_2 = {
        options: {
            chart: {
                type: 'column',
                inverted: false,
                options3d: {
                    enabled: true,
                    alpha: 0,
                    beta: 0,
                    depth: 20,
                    viewDistance: 25
                }
            },
            tooltip: {
              shared: true,
              valuePrefix: "R$ ",
              useHTML: $scope.tooltip_html
            },
          legend: {
            enabled: true
          }
        },
        xAxis: {
            categories: [],
            title: {
                text: null
            }
        },
        yAxis: {
            min: 0,
            title: {
                text: 'Valor em R$',
                align: 'high'
            },
            labels: {
                overflow: 'justify'
            }
        },
        plotOptions: {
            bar: {
                dataLabels: {
                    enabled: true
                }
            }
        },
        series: [{
            name: "Inicial",
            data: []
        },{
            name: "Atualizado",
            data: []
        },{
            name: "Empenhado",
            data: []
        },],
        title: {
            text: ''
        },
        loading: false
    }



    $scope.chart_3 = {
       options: {
          chart: {
              plotBackgroundColor: null,
              plotBorderWidth: null,
              plotShadow: false,
              type: 'pie'
          },
          title: {
              text: ''
          },
          tooltip: {
              pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>',
              useHTML: $scope.tooltip_html
          },
          legend: {
                align: 'left',
                layout: 'vertical',
                verticalAlign: 'top',
                x: 40,
                y: 0,
                labelFormatter: function() {
                    return $filter('titlecase')(this.name) + " - R$ " + Highcharts.numberFormat(this.y,2) + " (" + this.percentage.toFixed(2) + "%)";
                }
            },
            plotOptions: {
              pie: {
                  allowPointSelect: true,
                  cursor: 'pointer',
                  dataLabels: {
                      enabled: false,
                      format: '<b>{point.name}</b>: {point.percentage:.1f} %',
                      style: {
                          color: (Highcharts.theme && Highcharts.theme.contrastTextColor) || 'black'
                      }
                  },
                  showInLegend: true
              }
          }
        },
        series: [{
            name: 'Fonte de Recurso',
            colorByPoint: true,
            data: []
        }]
    }



    $scope.chart_4 = {
       options: {
          chart: {
              plotBackgroundColor: null,
              plotBorderWidth: null,
              plotShadow: false,
              type: 'pie'
          },
          title: {
              text: ''
          },
          tooltip: {
              pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>',
              useHTML: $scope.tooltip_html
          },
          legend: {
                align: 'left',
                layout: 'vertical',
                verticalAlign: 'top',
                x: 40,
                y: 0,
                labelFormatter: function() {
                    return $filter('titlecase')(this.name) + " - R$ " + Highcharts.numberFormat(this.y,2) + " (" + this.percentage.toFixed(2) + "%)";
                }
            },
            plotOptions: {
              pie: {
                  allowPointSelect: true,
                  cursor: 'pointer',
                  dataLabels: {
                      enabled: false,
                      format: '<b>{point.name}</b>: {point.percentage:.1f} %',
                      style: {
                          color: (Highcharts.theme && Highcharts.theme.contrastTextColor) || 'black'
                      }
                  },
                  showInLegend: true
              }
          }
        },
        series: [{
            name: '',
            colorByPoint: true,
            data: []
        }]
    }





    $scope.orgaos = [];
    $scope.localizacoes = [];

    $scope.options = {
      tooltipTemplate : function (label) {
        return label.label + ': R$ ' +    label.value.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ".");
       } ,
       multiTooltipTemplate : function (label) {
        return label.datasetLabel + ': R$ ' +    label.value.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ".");
       } ,
        responsive: true,
        maintainAspectRatio: true,
        barDatasetSpacing: 1,
        barShowStroke: true,
        barStrokeWidth : 2,
        barValueSpacing : 5,
        legendTemplate: "<ul class=\"<%=name.toLowerCase()%>-legend\"><% for (var i=0; i<datasets.length; i++){%><li><span style=\"background-color:<%=datasets[i].strokeColor%>\"></span><%if(datasets[i].label){%><%=datasets[i].label%><%}%></li><%}%></ul>"
    };


    init(2016);
    changeUnidades("01000");


    $scope.update = function() {
      changeUnidades($scope.selectedItem);
    }

    $scope.updateDate = function() {
      updateCharts();
    }

    $scope.updateLocalizacao = function() {
      ProgramasTrabalho.get($scope.selectedLocation).then(programasTrabalhoSuccessFn, ErrorFn);
      setDsLocation($scope.selectedLocation);
      function programasTrabalhoSuccessFn(data, status, headers, config) {
         var array = data.data.results;
         if(array != undefined){
           $scope.chart_4.series[0].data = [];
           $scope.chart_4.series[0].name = "Programa de Trabalho";
           for(var i=0; i < array.length; i++){
            if(array[i].vl_atualizado != null){
              $scope.chart_4.series[0].data.push({name: array[i].ds_programa_trabalho, y: array[i].vl_atualizado});
            }
           }
         }
      }

      function ErrorFn(data, status, headers, config) {
          Snackbar.error(data.error);
        }
    }

    function setDsOrgao(orgao){
        Orgaos.get(orgao).then(orgaosSuccessFn, orgaosErrorFn);
        function orgaosSuccessFn(data, status, headers, config) {
          if(data.data.results != undefined){
              $scope.orgaoSelected =  data.data.results[0].ds_orgao;
          }
        }

        function orgaosErrorFn(data, status, headers, config) {
          Snackbar.error(data.error);
        }
    }

    function setDsLocation(location){
        Localizacoes.get(location).then(localizacoesSuccessFn, ErrorFn);
        function localizacoesSuccessFn(data, status, headers, config) {
          if(data.data.results != undefined){
              $scope.dsLocalizacaoSelected =  data.data.results[0].ds_localizacao;
          }
        }

        function ErrorFn(data, status, headers, config) {
          Snackbar.error(data.error);
        }
    }

    function updateCharts(){
         UnidadesOrcamentarias.all($scope.selectedDate).then(unidadesOrcamentariasSuccessFn, ErrorFn);

         function unidadesOrcamentariasSuccessFn(data, status, headers, config) {
             var array = data.data.results;
             var inicial = 0.0;
             var atualizado = 0.0;
             var empenhado = 0.0;
             for(var i=0; i < array.length; i++){
                inicial = inicial + array[i].vl_inicial;
                atualizado = atualizado + array[i].vl_atualizado;
                empenhado = empenhado + array[i].vl_empenhado;
             }
             $scope.vl_inicial_geral = inicial;
             $scope.vl_atualizado_geral = atualizado;
             $scope.vl_empenhado_geral = empenhado;
             $scope.chart_1.series[0].data = [inicial, inicial, inicial];
             $scope.chart_1.series[1].data = [atualizado, atualizado, atualizado];
             $scope.chart_1.series[2].data = [empenhado, empenhado, empenhado];
          }

          function ErrorFn(data, status, headers, config) {
            Snackbar.error(data.error);
          }
    }

    function init(ano){
      Orgaos.all().then(orgaosSuccessFn, ErrorFn);
      FontesRecurso.all().then(fontesRecursoSuccessFn, ErrorFn);
      UnidadesOrcamentarias.all(ano).then(unidadesOrcamentariasSuccessFn, ErrorFn);
      Localizacoes.all().then(localizacoesSuccessFn, ErrorFn);

      function orgaosSuccessFn(data, status, headers, config) {
         $scope.orgaos = data.data.results;
      }

      function localizacoesSuccessFn(data, status, headers, config) {
         var array = data.data.results;
         $scope.localizacoes = [];
         $scope.chart_4.series[0].data = [];
         $scope.chart_4.series[0].name = "Localização";
         for(var i=0; i < array.length; i++){
          if(array[i].vl_atualizado != null){
            $scope.localizacoes.push(array[i]);
            $scope.chart_4.series[0].data.push({name: array[i].ds_localizacao, y: array[i].vl_atualizado});
          }
         }
      }

      function ErrorFn(data, status, headers, config) {
        Snackbar.error(data.error);
      }

      function fontesRecursoSuccessFn(data, status, headers, config) {
         var array = data.data.results;
         $scope.chart_3.series.data = [];
         for(var i=0; i < array.length; i++){
          if(array[i].vl_atualizado != null){
            $scope.chart_3.series[0].data.push({name: array[i].ds_fonte_recurso, y: array[i].vl_atualizado});
          }
         }
      }

      function unidadesOrcamentariasSuccessFn(data, status, headers, config) {
         var array = data.data.results;
         var inicial = 0.0;
         var atualizado = 0.0;
         var empenhado = 0.0;
         for(var i=0; i < array.length; i++){
            inicial = inicial + array[i].vl_inicial;
            atualizado = atualizado + array[i].vl_atualizado;
            empenhado = empenhado + array[i].vl_empenhado;
         }
         $scope.vl_inicial_geral = inicial;
         $scope.vl_atualizado_geral = atualizado;
         $scope.vl_empenhado_geral = empenhado;
         $scope.chart_1.series[0].data = [inicial, inicial, inicial];
         $scope.chart_1.series[1].data = [atualizado, atualizado, atualizado];
         $scope.chart_1.series[2].data = [empenhado, empenhado, empenhado];
      }

    }

    function changeUnidades(id_orgao) {
      if(id_orgao != "" && id_orgao != undefined){
        setDsOrgao(id_orgao);
        UnidadesOrcamentarias.get(id_orgao,$scope.selectedDate).then(unidadesOrcamentariasSuccessFn, unidadesOrcamentariasErrorFn);
      }

      function unidadesOrcamentariasSuccessFn(data, status, headers, config) {
         var array = data.data.results;
         $scope.chart_2.series[0].data = [];
         $scope.chart_2.series[1].data = [];
         $scope.chart_2.series[2].data = [];
         $scope.chart_2.xAxis.categories = [];
         var inicial = [];
         var atualizado = [];
         var empenhado = [];
         if(array != undefined){
           for(var i=0; i < array.length; i++){
              $scope.chart_2.xAxis.categories.push(array[i].nm_mnemonico);
              $scope.chart_2.series[0].data.push(array[i].vl_inicial);
              $scope.chart_2.series[1].data.push(array[i].vl_atualizado);
              $scope.chart_2.series[2].data.push(array[i].vl_empenhado);
           }
        }
      }

      function unidadesOrcamentariasErrorFn(data, status, headers, config) {
        Snackbar.error(data.error);
      }
    }

  }
})();
