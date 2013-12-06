
function GetAppCollapsibleContent(containername,appList)
{
    var htmlContent="";
    var appNames=[];
    var usages=[];
    var allocated=[];
    $.each(appList,function(index,appobj){
        $.each(appobj.apps,function(index,app){
                appNames.push(app.name);
                usages.push(app.weekly_usage);
                
        });
        htmlContent+='</div></div></div>';
    });
    
    $(containername).highcharts({
        chart: {
                type: 'bar'
            },
            title: {
                text: 'Weekly App Usage'
            },
            xAxis: {
                categories: appNames
            },
            yAxis: {
                min: 0,
                title: {
                    text: 'Weekly usage'
                }
            },
            legend: {
                backgroundColor: '#FFFFFF',
                reversed: true
            },
            plotOptions: {
                bar: {
                    dataLabels: {
                        enabled: true
                    }
                }
            },
                series: [{
                name: 'Used',
                data: usages,
                color:'RED'
            }]
    });
    
    return htmlContent;
}

function GetDeviceCollapsibleContent(devList)
{
    var htmlContent="";
    $.each(devList,function(index,devobj){
        htmlContent+='<div data-role="collapsible" class="no_wrap widget uib_w_3" data-uib="jquery_mobile/collapsible"> \
    <h4>'+devobj.device_name+'</h4> \
    <div class="col uib_col_2 single-col" data-uib="layout/col"> \
            <div class="widget-container content-area vertical-col">';
        htmlContent+='<div class="widget uib_w_6 no_wrap with-label d-margins" data-uib="jquery_mobile/slider"> \
                    <label class="narrow-control label-inline">Weekly Use</label> \
                    <div class="wide-control"> \
                        <input type="range" value="10" min="0" max="20" step="1"> \
                    </div> \
                </div> ';
        htmlContent+='</div></div></div>';
    });
    console.log(htmlContent);
    return htmlContent;
}

function GetUserCollectionContent()
{
    
}

function GetUsers()
{
    return getData("http://apptime.herokuapp.com/apptime/users");
}

function GetDevices(userid)
{
    return getData("http://apptime.herokuapp.com/apptime/user/"+userid+"/devices");
}

function GetApps(userid)
{
    return getData("http://apptime.herokuapp.com/apptime/user/"+userid+"/apps/usage");
}

function enableCurfew(userid)
{
    //Hardcoding
    return postData("http://apptime.herokuapp.com/apptime/user/Sally/curfew")
}


function getData(serviceUrl)
{
    var jsonObj;
    $.ajax({
        async:false,
        type:'GET',
        url:serviceUrl,
        dataType: "json",
        success: function(data,status,xhr){
            jsonObj = data;
        },
        error:function(xhr,status,error){
            console.error(status+':'+error);
            jsonObj=null;
        }
    });
    return jsonObj;
}

function postData(serviceUrl)
{
    var jsonObj;
    $.ajax({
        async:true,
        type:'POST',
        url:serviceUrl,
        dataType: "json",
        error:function(xhr,status,error){
            console.error(status+':'+error);
            jsonObj=null;
        }
    });
    return jsonObj;
}