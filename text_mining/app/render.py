# -*- coding: utf-8 -*-

import query
import re
from json import dumps 



def http_header():
    print "Content-type: text/html; charset=utf-8"
    print 

def render_co_articles(word1, word2):
    # TODO: match entire word, not part of word
    # example: "rate" should not match "accurate"
    # file_path = "/tmp/tmp_co_articles.html"
    articles = query.get_co_articles(word1, word2)
    li1 = [ x for x in word1.replace('-', ' ').split(' ') if x]
    li2 = [ x for x in word2.replace('-', ' ').split(' ') if x]

    #p1 = re.compile('([^\s])(' + u'|'.join(li1) + ')([$\s])')
    p1 = re.compile('(?i)(' + u'|'.join(li1) + ')')
    p2 = re.compile('(?i)(' + u'|'.join(li2) + ')')
    color1 = '#F0D8A7'
    color2 = '#A7BFF0'
    #with open(file_path, 'w') as f:
    print '<t1 style="height: 100%; width: 100%;"> {} vs. {}'.format(word1, word2)
    print '<p> Cooccurrence : %d</p>' % len(articles)
    for article in articles:
        print '<hr>'
        print u'<t3> {} <t3>'.format(article[0]).encode('utf-8')
        print '<p> see with PMID on PubMed: <a href="http://www.ncbi.nlm.nih.gov/pubmed/?term={0}">{0}</a> </p>'.format(article[1])
        for paragraph in article[2]:
            paragraph = p1.sub(r'<span style="background-color:{};">\1</span>'.format(color1), paragraph)
            paragraph = p2.sub(r'<span style="background-color:{};">\1</span>'.format(color2), paragraph)
            print u'<p>{}</p>'.format(paragraph).encode('utf-8')
     # webbrowser.open('file://' + file_path)

def html_header(s='''
     <script src="html/jquery.min.js"></script>
    <link href="html/jquery-ui/css/smoothness/jquery-ui-1.10.4.custom.css" rel="stylesheet">
    <style>
    .cooccur {
    float:right;
    color: #999999;
    }
    
    .ui-autocomplete {
    height: 400px;
    max-width: 300px;
    overflow-y: scroll;
    overflow-x: hidden;
    }
    
    a:hover
    {
        font-size: 30;
    }
    
    </style>
    
    <script src="html/jquery-ui/js/jquery-1.10.2.js"></script>
    <script src="html/jquery-ui/js/jquery-ui-1.10.4.custom.js"></script>
    <script src="html/svg-pan-zoom.js"></script>
   
    <script>
    
    
        var li = %s;
    
        var update_st_autocomplete = function() {
            console.log("called update!");
            var ft = $("#ft").val();
            //var ref =
            $.get('suggestions.py',{term:ft},function(data){
            $("#st").autocomplete({
                source : data
            }).data("ui-autocomplete")._renderItem = function(ul, item){
                return $("<li>")
                .append($("<a>").text(item.value).append($('<span">').
                    addClass("cooccur").text(item.co)))
                .appendTo(ul);
                };
            },'json');
    }
    
    $(document).ready(function(){
        $("#ft").autocomplete({
            source : li
        });
    
        $("#gt").autocomplete({
            source : li
        });
    
        update_st_autocomplete();
        $("#ft").on("focusout", update_st_autocomplete);
        svgPanZoom.init({'minZoom':'0.3'});
    });
    
    </script>
    <link href='http://fonts.googleapis.com/css?family=Cinzel+Decorative:400,700,900' rel='stylesheet' type='text/css'>
    <link rel="stylesheet" type="text/css" href="HTML files/css/primary.css">
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <meta http-equiv="Content-Style-Type" content="text/css">
    
    
'''):
    print '<head>{}</head>'.format(s % dumps([x for x in query.get_file_list()]))

def render_div_search(gt='', ft='', st=''):
    print '''
        <div class="search">
        
        <nav>
            <div class = "menu-item">
                <h3> Global View </h3>
        
                <form action="../../one_term.py">
                    <input type = "radio" name = "GraphMode" value = "all"> Most Connected
                    </br>
                    '''
    for (id) in query.get_cluster():
        print '''
            <input type = "radio" name = "GraphMode" value = "cl{id}"> Cluster {id}
            </br>
            '''.format(id = id)
    print '''
                    <input type = "submit" value = "View">
                </form>
            </div>
		
            <div class = "menu-item">
                <h3> Subgraph </h3>
                <form action="../../one_term.py" >
                    <input list = "terms" id = "gt" placeholder = "Subgraph Term" name = "GraphTerm" value="{GraphTerm}">
                    <datalist id = "terms">
                    '''.format(GraphTerm = gt)
    for term in query.terms():
        print '''
            <option value = "{term}">
            '''.format(term = term)
    print '''
                       </datalist>
                    </br>
                    <input type = "radio" name = "GraphMode" value = "text"> Text View
                    </br>
                    <input type = "radio" name = "GraphMode" value = "simple" checked = "checked"> Simple Graph View
                    </br>
                    <input type = "radio" name = "GraphMode" value = "complete"> Complete Graph View
                    </br>
                    <input type = "submit" value = "View">
                </form>
            </div>
		
            <div class = "menu-item">
                <h3> Co-occurrence of 2 Terms </h3>
                <form action="../../co_articles.py">
                    <input type = "text" id = "ft" value = "" placeholder = "First Term" name = "FirstTerm">
                    </br>
                    <input type = "text" id = "st" value = "" placeholder = "Second Term" name = "SecondTerm">
                    </br>
                    <input type = "submit" value = "View">
                </form>
            </div>
            </br>
            <div class = "menu-item">
                <form action="../../one_term.py" >
                <input type = "submit" name = "all" value = "List all Terms">
                </form>
            </div>
        </nav>
        
        </div>
        
        
		<div class="content">
		
    '''.format(FirstTerm=ft, SecondTerm=st)

def list_terms():
    for term in query.terms():
        print '''
            <a href = "/one_term.py?GraphTerm={term}&GraphMode=simple"> {term} </a>
            '''.format(term=term)
        print "<br/>"


def render_datalist( list_id='terms', list_id2='terms2'):
    print '<datalist id="{}">'.format(list_id)
    for term in query.get_file_list():
        print '<option value="{}">'.format(term)
    print '</datalist>'
