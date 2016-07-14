import wikipedia
import MySQLdb
import threading
from entitylink import *

def pagerank(entitydic,edges,nodes):
	G = nx.DiGraph()
	G.add_nodes_from(nodes)
	G.add_edges_from(edges)
	#nx.draw(G,with_labels = True)
	#plt.show()
	pr = nx.pagerank(G)
	predict = {}

	for key in entitydic.keys():
		value = 0
		for canentity in entitydic[key]:
			entityvalue = pr[canentity]
			if entityvalue>value:
				value = entityvalue
				predictentity = canentity
		predict[key] = predictentity
	return predict

if __name__ == '__main__':
	#entitydic = {'Good_Doctor': ['The_Good_Doctor', 'The_good_doctor_(phrase)', 'The_Good_Doctor_(Law_&_Order:_Criminal_Intent)', 'The_Good_Doctor_(play)', 'The_Good_Doctor_(1939_film)', 'Good_Doctor_(TV_series)', 'Good_Doctor_(advertisement)', 'The_Good_Doctor_(2011_film)', '2013_KBS_Drama_Awards', 'Bon_Docteur_Nunatak'], 'Mitt': ['Moscow_Institute_of_Thermal_Technology', 'Mitt', 'Mitt_Romney', 'Mitt_(film)', 'Statewide_opinion_polling_for_the_United_States_presidential_election,_2012', 'T\xc3\xba_alfagra_land_m\xc3\xadtt', 'I_mitt_hj\xc3\xa4rta', 'Early/Mid_2012_statewide_opinion_polling_for_the_United_States_presidential_election,_2012', 'Nationwide_opinion_polling_for_the_United_States_presidential_election,_2012', 'Statewide_opinion_polling_for_the_Republican_Party_presidential_primaries,_2008'], 'Santorum': ['Rick_Santorum', 'Campaign_for_"santorum"_neologism', 'Santorum_(disambiguation)', 'Rick_Santorum_presidential_campaign,_2016', "Rick_Santorum's_views_on_homosexuality", 'Rick_Santorum_presidential_campaign,_2012', 'Santorum_Amendment', 'United_States_Senate_election_in_Pennsylvania,_2006', 'United_States_Senate_election_in_Pennsylvania,_1994', 'United_States_Senate_election_in_Pennsylvania,_2000'], 'Romney': ['Romney', 'Mitt_Romney', 'George_W._Romney', 'George_Romney', 'Romney_Literary_Society', 'Literary_Hall', 'Mitt_Romney_presidential_campaign,_2012', 'Old_Romney', 'HMS_Romney_(1708)', 'Ann_Romney'], 'Huckabee': ['Huckabee', 'Mike_Huckabee', 'Mike_Huckabee_presidential_campaign,_2016', 'Mike_Huckabee_presidential_campaign,_2008', 'Who_Made_Huckabee?', 'Statewide_opinion_polling_for_the_Republican_Party_presidential_primaries,_2008', 'Huckabee_(surname)', 'Political_positions_of_Mike_Huckabee', 'David_Huckabee', 'Nationwide_opinion_polling_for_the_Republican_Party_2008_presidential_primaries'], 'Obama': ['Barack_Obama', 'Barack_Obama_"Hope"_poster', 'Michelle_Obama', 'Inauguration_of_Barack_Obama', 'First_inauguration_of_Barack_Obama', 'Family_of_Barack_Obama', 'I_Got_a_Crush..._on_Obama', 'Barack_Obama_in_comics', 'Obama_logo', 'Political_positions_of_Barack_Obama'], 'Newt': ['Hogwarts', 'Newt', 'Northern_crested_newt', 'Newt_Gingrich', 'Newt_(Hollyoaks)', 'Japanese_fire_belly_newt', 'Fire_belly_newts', 'Eastern_newt', 'Salamandridae', 'Black-spotted_newt'], 'Gingrich': ['Gingrich', 'Newt_Gingrich', "Bauer's_Lexicon", 'Candace_Gingrich', 'Mauree_Gingrich', 'Callista_Gingrich', 'Newt_Gingrich_presidential_campaign,_2012', 'Arnold_Gingrich', '1945_(Gingrich_and_Forstchen_novel)', 'Nationwide_opinion_polling_for_the_Republican_Party_2008_presidential_primaries']}
	entitydic = {'Good_Doctor': ['The_Good_Doctor', 'Good_Doctor_(advertisement)', 'The_Good_Doctor_(2011_film)'], 'Mitt': ['Mitt_(film)','Mitt_Romney'], 'Santorum': ['Rick_Santorum', 'Campaign_for_"santorum"_neologism', 'Santorum_(disambiguation)', 'Rick_Santorum_presidential_campaign,_2016', "Rick_Santorum's_views_on_homosexuality", 'Rick_Santorum_presidential_campaign,_2012', 'Santorum_Amendment', 'United_States_Senate_election_in_Pennsylvania,_2006', 'United_States_Senate_election_in_Pennsylvania,_1994', 'United_States_Senate_election_in_Pennsylvania,_2000'], 'Romney': ['Romney', 'Mitt_Romney', 'George_W._Romney', 'George_Romney', 'Romney_Literary_Society', 'Literary_Hall', 'Mitt_Romney_presidential_campaign,_2012', 'Old_Romney', 'HMS_Romney_(1708)', 'Ann_Romney'], 'Huckabee': ['Huckabee', 'Mike_Huckabee', 'Mike_Huckabee_presidential_campaign,_2016', 'Mike_Huckabee_presidential_campaign,_2008', 'Who_Made_Huckabee?', 'Statewide_opinion_polling_for_the_Republican_Party_presidential_primaries,_2008', 'Huckabee_(surname)', 'Political_positions_of_Mike_Huckabee', 'David_Huckabee', 'Nationwide_opinion_polling_for_the_Republican_Party_2008_presidential_primaries'], 'Obama': ['Barack_Obama', 'Barack_Obama_"Hope"_poster', 'Michelle_Obama', 'Inauguration_of_Barack_Obama', 'First_inauguration_of_Barack_Obama', 'Family_of_Barack_Obama', 'I_Got_a_Crush..._on_Obama', 'Barack_Obama_in_comics', 'Obama_logo', 'Political_positions_of_Barack_Obama'], 'Newt': ['Hogwarts', 'Newt', 'Northern_crested_newt', 'Newt_Gingrich', 'Newt_(Hollyoaks)', 'Japanese_fire_belly_newt', 'Fire_belly_newts', 'Eastern_newt', 'Salamandridae', 'Black-spotted_newt'], 'Gingrich': ['Gingrich', 'Newt_Gingrich', "Bauer's_Lexicon", 'Candace_Gingrich', 'Mauree_Gingrich', 'Callista_Gingrich', 'Newt_Gingrich_presidential_campaign,_2012', 'Arnold_Gingrich', '1945_(Gingrich_and_Forstchen_novel)', 'Nationwide_opinion_polling_for_the_Republican_Party_2008_presidential_primaries']}
	#entitydic = {'Good_Doctor': ['Good_Doctor', 'Good_doctor', 'Ron_Paul','Suzhou'], 'Mitt': ['Mitt', 'MITT', 'Mitt.', 'Gr-R/Mitt', 'Mitt._dt._Pat.-anw.', 'Mitt-meet_merger', 'Mitt_Romney'], 'Santorum': ['Santorum', "Santorum's_Google_problem", 'Santorum-Savage_neologism_campaign_Google_bomb_problem_controversy', "Santorum's_Google_Problem", 'Campaign_for_"santorum"_neologism', 'Campaign_for_"Santorum"_slur', 'Campaign_for_"Santorum"_neologism', 'Rick_Santorum'], 'Romney': ["Romney's", 'Romney,_PA', 'Romney,_IN', 'Romney,_TX', 'Romney', 'Romney,_WV', 'Romney/Ryan', 'Mitt_Romney'], 'Huckabee': ['Huckabee', 'Mike+huckabee', 'Mike_Huckabee'], 'Obama': ['OBAMA!', 'Obama', 'OBAMA', 'Obama-j\xc5\x8d', 'Obama,_the_Menteng_Kid', "Obama's_100_Days", "Obama's_Birthday", 'Barack_Obama'], 'Newt': ['NEWT', 'Newt.org', 'Newt', 'Newt,_Alpine', 'Python-newt', 'Newt,_Kentucky', 'Newton_"Newt"_Livingston_IV', 'Newt_Gingrich'], 'Gingrich': ['Gingrich', 'Gingrich,_Newt', 'Newt_Gingrich']}
	targetlist = [['Romney','Mitt_Romney'],['Santorum','Rick_Santorum'],['Huckabee','Mike_Huckabee'],['Gingrich','Newt_Gingrich'],['Good_Doctor','Ron_Paul'],['Mitt', 'Mitt_Romney'],['Obama','Barack_Obama'],['Newt','Newt_Gingrich']]
	entitypairarray = getEntityPair1(entitydic)
	patharray = getPairArrayPath1(entitypairarray)
	edges,nodes = getEdges(patharray)
	#print edges
	print "edges:" + str(len(nodes))
	tm = 0
	cn = 0
	starttime0 = dt.datetime.now()
	for m in entitydic.items():
		for n in m[1]:
			nodes.append(n)
	nodes = list(set(nodes))
	print "nodes:" + str(len(nodes))
	predict = getGraphByStandardPagelink1(entitydic,edges,nodes)
	#predict = getGraphByGreedSearch(entitydic,edges,nodes)
	print predict
	for mention,target in targetlist:
		tm += 1
		if predict[mention] == target:
			cn += 1
		print "mention:" + mention + "   target:" + target + "     predict:" + predict[mention]
	endtime0 = dt.datetime.now()
	print "doc_totalnumber:" + str(tm)
	print "doc_correctnumber:" + str(cn)
	print "doc_precious:" + str(float(cn)/tm)
	print "doc_runtime:" + str(endtime0 - starttime0)