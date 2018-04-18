from wikipediaapi import Wikipedia


class Post:
    def __init__(self, team_names='', team_colors='',
                 team1_players='', team2_players='',
                 options='', header='', question='',
                 twTags=''):
        if team_names == '' or team_colors == '' or team1_players == '' or team2_players == '':
            return

        if options == '' or header == '' or question == '':
            return

        self.listitems = list(options)
        self.header = str(header)
        self.question = str(question)
        self.wiki = Wikipedia('en')
        self.team_names = list(team_names)
        self.team_colors = list(team_colors)
        self.team1_players = list(team1_players)
        self.team2_players = list(team2_players)
        self.twTags = list(twTags)

    def getWikiUrl(self, player_name=''):
        if player_name == '':
            return None

        page_py = self.wiki.page(player_name)
        if page_py.exists() is False:
            return None

        return page_py.fullurl

    @staticmethod
    def tag(name, *content, style=None, href=None, **attrs):
        if style is not None:
            attrs['style'] = style

        if href is not None:
            attrs['href'] = href

        if attrs:
            attr_str = ''.join(' %s="%s"' % (attr, value)
                               for attr, value
                               in sorted(attrs.items()))
        else:
            attr_str = ""

        if content:
            return '\n'.join('<%s%s>%s</%s>' %
                             (name, attr_str, c, name) for c in content)
        else:
            return '<%s%s />' % (name, attr_str)

    def formatApi(self):
        http_part = "http --auth : --form POST http://www.tactification.com/api_rt/v1.0/new_post "
        question_tag = self.tag('div', self.question, style='color:black')
        br1 = self.tag('br')

        li_items = str()
        for item in self.listitems:
            li_items += ''.join(self.tag('li', item))

        ul = self.tag('ul', li_items)
        div1 = self.tag('div', ul, style='color:black')

        starring_tag = self.tag('div', "Starring:", style='color:black')

        team1_url = self.getWikiUrl(self.team_names[0])
        if team1_url is None:
            print(self.team_names[0])
            return

        a_team1 = self.tag('a', self.team_names[0], href=team1_url) + ': '
        a_items = str()
        for item in self.team1_players:
            print(item)
            player_url = self.getWikiUrl(item[0])
            if player_url is None:
                print(item)
                return

            a_items += ''.join(self.tag('a', item[0], href=player_url) + '(' + str(item[1]) + '),')

        a_items.rstrip(',')

        i_team1 = self.tag('i', a_team1+a_items, style="color:" + str(self.team_colors[0]))
        team2_url = self.getWikiUrl(self.team_names[1])
        if team2_url is None:
            print(self.team_names[1])
            return

        a_team2 = self.tag('a', self.team_names[1], href=team2_url) + ': '
        a_items = str()
        for item in self.team2_players:
            player_url = self.getWikiUrl(item[0])
            if player_url is None:
                print(item)
                return

            a_items += ''.join(self.tag('a', item[0], href=player_url) + '(' + str(item[1]) + '),')

        a_items.rstrip(',')

        i_team2 = self.tag('i', a_team2+a_items, style="color:" + str(self.team_colors[1]))
        header = " header={!r} ".format(self.header)
        twTag = (" twTags='#{}, #{}, #{}' ".format(*self.twTags))
        end_part = "tactical_gif@home_img.jpg tactical_pic_1750@with_help_msg.jpg tactical_pic_1575@with_help_msg_75.jpg tactical_pic_875@with_help_msg_50.jpg"
        final_command = http_part + "body='" + question_tag + br1 + div1 + starring_tag + i_team1 + br1 + i_team2 + "'" + header + twTag + end_part
        print(final_command)


teams = ['Juventus', 'Real Madrid']
team_colors = ['#FFD700', '#00C5CD']
team1_players = [('Pjanic', '6'), ('De Sciglio', '2'), ('Douglas Costa', '7'), ('Higuain', '9'), ('Matuidi', '8'), ('Sami Khedira', '10'), ('Mandzukic', '11')]
team2_players = [('Isco', '10'), ('Luca Modric', '8'), ('Toni Kroos', '11'), ('Casemiro', '6'), ('Marcelo', '3'), ('Carvajal', '2'), ('varane', '5'), ('Vallejo', '4')]
question = 'Try to predict the move in the game from this situation?'
options = ['With Real Madrid in numerical disadvantage, how do you expect each defenders react in this situation?', 'How Juventus can take advantage of the numerical superiority?', 'Share all tactical thoughts you have in this situation from Real Madrid Vs Juventus game']
header = "Ft: Real Madrid vs Juventus"
twTags = ['juve', 'realmadrid', 'UCL']
obj = Post(team_names=teams, team_colors=team_colors, team1_players=team1_players, team2_players=team2_players, options=options, header=header, question=question, twTags=twTags)
obj.formatApi()

