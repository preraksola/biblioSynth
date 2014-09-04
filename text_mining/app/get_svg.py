    #!/usr/bin/env /usr/bin/python
# -*- coding: utf-8 -*-

import igraph
import query

def line_width(w):
    if w > 10:
        return 3
    elif w > 3:
        return 2;
    else:
        return 1;

def get_svg_complete(args):
    gt = ''
    mode = ''
    if 'GraphTerm' in args:
        gt = args['GraphTerm']
    graphml_path = '/Users/utilisateur/Documents/workspace/Internship/text_mining/graphe/{}{}.graphml'.format(gt.replace(' ', '_'), mode)
#   print graphml_path
    svg_path =  '/Users/utilisateur/Documents/workspace/Internship/text_mining/data/my_cloud_colored.svg'
    
    margin = 50
    width = 1600
    height = 2500
    try:
        g = igraph.Graph.Read_GraphML(graphml_path)
    except IOError:
        return '<p>The graph of {gt} is unavailable.</p>'.format(gt=gt)
    cl = g.community_walktrap().as_clustering()
    template = ''
    f = open(svg_path, 'r')
    template = f.read()
    f.close()
    vs = len(g.vs)
    svg_layout = g.layout('kk')
    svg_layout.fit_into(igraph.BoundingBox(width, height))
    
    list_datasets = []
    list_shadows = []
    list_links = []
    for i in xrange(vs):
        list_datasets.append('''
        <a id="dataset-{name}" class="dataset {gp}" xlink:href="co_articles.py?FirstTerm={gt}&SecondTerm={nr}" transform="translate({coord[0]} {coord[1]})" >
            <circle r="42"></circle>
            <text class="label" id="t-{name}" x="0" y="3" fontsize="8">{name}
            </text>
        </a>
        '''.format(name=g.vs['name'][i], coord=svg_layout[i], gp='' if i == 0 else 'g' + str(cl.membership[i]), gt=gt, nr=g.vs['name'][i].replace('_', ' ') ))
        #list_shadows.append('''
        #<use id="shadow-{name}" x="{coord[0]}" y="{coord[1]}" xlink:href="#shadow-size5"></use>
#'''.format(name=g.vs['name'][i], coord=svg_layout[i]))
    
    for edge in g.es:
        source = edge.source
        target = edge.target
        list_links.append('''
            <line x1="{coord1[0]}" y1="{coord1[1]}" x2="{coord2[0]}" y2="{coord2[1]}" marker-end="url(#arrowhead-end-width{w})" class="links width{w} {fromcenter} from-{name1} to-{name2}"></line>
        '''.format(name1=g.vs['name'][source], name2=g.vs['name'][target], w=line_width(edge['weight']), coord1=svg_layout[source], coord2=svg_layout[target], fromcenter='fromcenter' if source == 0 else '' ))
    
    
    
    #print '''<div id="container" style="height:2000px; width:1000px;">'''
    return template.format(layer_datasets=u''.join(list_datasets), layer_shadows=u''.join(list_shadows), layer_links=u''.join(list_links))
    #print '''</div>'''

def get_svg_simple(args):
    gt = ''
    mode = 'Simple'
    if 'GraphTerm' in args:
        gt = args['GraphTerm']
    graphml_path = '/Users/utilisateur/Documents/workspace/Internship/text_mining/graphe/{}{}.graphml'.format(gt.replace(' ', '_'), mode)
    #   print graphml_path
    svg_path =  '/Users/utilisateur/Documents/workspace/Internship/text_mining/data/my_cloud_colored.svg'
    
    margin = 50
    width = 1600
    height = 2500
    try:
        g = igraph.Graph.Read_GraphML(graphml_path)
    except IOError:
        return '<p>The graph of {gt} is unavailable.</p>'.format(gt=gt)
    cl = g.community_walktrap().as_clustering()
    template = ''
    f = open(svg_path, 'r')
    template = f.read()
    f.close()
    vs = len(g.vs)
    svg_layout = g.layout('kk')
    svg_layout.fit_into(igraph.BoundingBox(width, height))

    list_datasets0 = []
    list_datasets1 = []
    list_datasets2 = []
    list_datasets3 = []
    list_datasets4 = []
    list_datasets5 = []
    list_datasets6 = []
    list_datasets = []
    list_shadows = []
    list_links = []

    for i in xrange(vs):
        color_id = query.list_content(g.vs['name'][i])
        g.vs[i]["c_id"] = color_id

    for i in xrange(vs):
        if (g.vs[i]["c_id"] == 1):
            list_datasets1.append('''
                <a id="dataset-{name}" class="dataset {gp}" xlink:href="co_articles.py?FirstTerm={gt}&SecondTerm={nr}" transform="translate({coord[0]} {coord[1]})" >
                <circle r="42" onmouseover="this.r='46;" style="filter: url(#shadow-filter5);"></circle>
                <text class="label" id="t-{name}" x="0" y="3" fontsize="8">{name}
                </text>
                </a>
                '''.format(name=g.vs['name'][i],coord=svg_layout[i], gp='sg' + str(g.vs["c_id"][i]), gt=gt, nr=g.vs['name'][i].replace('_', ' ') ))
        elif (g.vs["c_id"][i] == 2):
            list_datasets2.append('''
                    <a id="dataset-{name}" class="dataset {gp}" xlink:href="co_articles.py?FirstTerm={gt}&SecondTerm={nr}" transform="translate({coord[0]} {coord[1]})" >
                    <circle r="42" onmouseover="this.r='46;" style="filter: url(#shadow-filter5);"></circle>
                    <text class="label" id="t-{name}" x="0" y="3" fontsize="8">{name}
                    </text>
                    </a>
                    '''.format(name=g.vs['name'][i], coord=svg_layout[i], gp='sg' + str(g.vs["c_id"][i]), gt=gt, nr=g.vs['name'][i].replace('_', ' ') ))
        elif (g.vs["c_id"][i] == 3):
            list_datasets3.append('''
                <a id="dataset-{name}" class="dataset {gp}" xlink:href="co_articles.py?FirstTerm={gt}&SecondTerm={nr}" transform="translate({coord[0]} {coord[1]})" >
                <circle r="42" style="filter: url(#shadow-filter5);"></circle>
                <text class="label" id="t-{name}" x="0" y="3" fontsize="8">{name}
                </text>
                </a>
                '''.format(name=g.vs['name'][i], coord=svg_layout[i], gp='sg' + str(g.vs["c_id"][i]), gt=gt, nr=g.vs['name'][i].replace('_', ' ') ))
        elif (g.vs["c_id"][i] == 4):
            list_datasets4.append('''
        <a id="dataset-{name}" class="dataset {gp}" xlink:href="co_articles.py?FirstTerm={gt}&SecondTerm={nr}" transform="translate({coord[0]} {coord[1]})" >
        <circle r="42" style="filter: url(#shadow-filter5);"></circle>
        <text class="label" id="t-{name}" x="0" y="3" fontsize="8">{name}
        </text>
        </a>
        '''.format(name=g.vs['name'][i], coord=svg_layout[i], gp='sg' + str(g.vs["c_id"][i]), gt=gt, nr=g.vs['name'][i].replace('_', ' ') ))
        elif (g.vs["c_id"][i] == 5):
            list_datasets5.append('''
        <a id="dataset-{name}" class="dataset {gp}" xlink:href="co_articles.py?FirstTerm={gt}&SecondTerm={nr}" transform="translate({coord[0]} {coord[1]})" >
        <circle r="42" style="filter: url(#shadow-filter5);"></circle>
        <text class="label" id="t-{name}" x="0" y="3" fontsize="8">{name}
        </text>
        </a>
        '''.format(name=g.vs['name'][i], coord=svg_layout[i], gp='sg' + str(g.vs["c_id"][i]), gt=gt, nr=g.vs['name'][i].replace('_', ' ') ))
        elif (g.vs["c_id"][i] == 6):
            list_datasets6.append('''
            <a id="dataset-{name}" class="dataset {gp}" xlink:href="co_articles.py?FirstTerm={gt}&SecondTerm={nr}" transform="translate({coord[0]} {coord[1]})" >
            <circle r="42" style="filter: url(#shadow-filter5);"></circle>
            <text class="label" id="t-{name}" x="0" y="3" fontsize="8">{name}
            </text>
            </a>
            '''.format(name=g.vs['name'][i], coord=svg_layout[i], gp='sg' + str(g.vs["c_id"][i]), gt=gt, nr=g.vs['name'][i].replace('_', ' ') ))
    
        else:
            list_datasets0.append('''
                <a id="dataset-{name}" class="dataset {gp}" xlink:href="co_articles.py?FirstTerm={gt}&SecondTerm={nr}" transform="translate({coord[0]} {coord[1]})" >
                <circle r="42" onmouseover="this.r='46;" style="filter: url(#shadow-filter5);"></circle>
                <text class="label" id="t-{name}" x="0" y="3" fontsize="8">{name}
                </text>
                </a>
                '''.format(name=g.vs['name'][i], coord=svg_layout[i], gp='sg' + str(g.vs["c_id"][i]), gt=gt, nr=g.vs['name'][i].replace('_', ' ') ))
            #  list_shadows.append('''
            #<use id="shadow-{name}" x="{coord[0]}" y="{coord[1]}" xlink:href="#shadow-size5"></use>
#'''.format(name=g.vs['name'][i], coord=svg_layout[i]))

    list_datasets.extend(list_datasets1)
    list_datasets.extend(list_datasets2)
    list_datasets.extend(list_datasets3)
    list_datasets.extend(list_datasets4)
    list_datasets.extend(list_datasets5)
    list_datasets.extend(list_datasets6)
    list_datasets.extend(list_datasets0)
    for edge in g.es:
        source = edge.source
        target = edge.target
        list_links.append('''
            <line x1="{coord1[0]}" y1="{coord1[1]}" x2="{coord2[0]}" y2="{coord2[1]}" marker-end="url(#arrowhead-end-width{w})" class="links width{w} {fromcenter} from-{name1} to-{name2}"></line>
            '''.format(name1=g.vs['name'][source], name2=g.vs['name'][target], w=line_width(edge['weight']), coord1=svg_layout[source], coord2=svg_layout[target], fromcenter='fromcenter' if source == 0 else '' ))
    
    
    
    #print '''<div id="container" style="height:2000px; width:1000px;">'''
    return template.format(layer_datasets=u''.join(list_datasets), layer_shadows=u''.join(list_shadows), layer_links=u''.join(list_links))
#print '''</div>'''

    
def get_svg_all(args):
    gt = ''
 
    #mode = '' if args['GraphMode'] == 'complete' else 'Simple'
    
    if 'GraphTerm' in args:
        gt = args['GraphTerm']
    
    if 'GraphMode' in args:
        mode = args['GraphMode']
    
    #graphml_path = '/home/salma/MATRICEFanny/text_mining/data/graphe_PTSD/{}{}.graphml'.format(gt.replace(' ', '_'), mode)
    '''
    if gt == "cluster1":
    	graphml_path = '/home/salma/warMATRICE/grapheVIP_cl00.graphml'
    else:
    	if gt == "cluster2":
    		graphml_path = '/home/salma/warMATRICE/grapheVIP_cl01.graphml'
    '''
    if mode == 'all':
        graphml_path = '/Users/utilisateur/Documents/workspace/Internship/text_mining/VIPGraph/grapheVIP.graphml'

    else:
        graphml_path = '/Users/utilisateur/Documents/workspace/Internship/text_mining/VIPGraph/grapheVIP_{id}.graphml'.format(id = mode)

#print graphml_path
    svg_path =  '/Users/utilisateur/Documents/workspace/Internship/text_mining/data/my_cloud_colored.svg'
    
    #print graphml_path
#margin = 50
    width = 1600
    height = 2500
    try:
        g = igraph.Graph.Read_GraphML(graphml_path)
    except IOError:
        return '<p>The graph of {ct} is unavailable.</p>'.format(gt=gt)
    cl = g.community_walktrap().as_clustering()
    template = ''
    f = open(svg_path, 'r')
    template = f.read()
    f.close()
    vs = len(g.vs)
    svg_layout = g.layout('kk')
    svg_layout.fit_into(igraph.BoundingBox(width, height))
    
    list_datasets = []
    list_shadows = []
    list_links = []
    for i in xrange(vs):
        list_datasets.append('''
        <a id="dataset-{name}" class="dataset {gp}" xlink:href="one_term.py?GraphTerm={nr}&GraphMode=simple" transform="translate({coord[0]} {coord[1]})" >
            <circle r="15"></circle>
            <text class="label" id="t-{name}" x="0" y="3" fontsize="8">{name}
            
            </text>
        </a>
        '''.format(name=g.vs['name'][i], coord=svg_layout[i], gp='' if i == 0 else 'g' + str(cl.membership[i]), gt=gt, nr=g.vs['name'][i].replace('_', ' ') ))
        list_shadows.append('''
        <use id="shadow-{name}" x="{coord[0]}" y="{coord[1]}" xlink:href="#shadow-size1"></use>
        '''.format(name=g.vs['name'][i], coord=svg_layout[i]))
    
    for edge in g.es:
        source = edge.source
        target = edge.target
        list_links.append('''
            <line x1="{coord1[0]}" y1="{coord1[1]}" x2="{coord2[0]}" y2="{coord2[1]}" marker-end="url(#arrowhead-end-width{w})" class="links width{w} {fromcenter} from-{name1} to-{name2}"></line>
        '''.format(name1=g.vs['name'][source], name2=g.vs['name'][target], w=line_width(edge['weight']), coord1=svg_layout[source], coord2=svg_layout[target], fromcenter='fromcenter' if source == 0 else '' ))
    
    
    
    #print '''<div id="container" style="height:2000px; width:1000px;">'''
    return template.format(layer_datasets=u''.join(list_datasets), layer_shadows=u''.join(list_shadows), layer_links=u''.join(list_links))
    #print '''</div>'''