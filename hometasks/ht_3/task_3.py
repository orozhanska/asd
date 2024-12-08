def word_frequency_counter(text):
    """
    Count the frequency of each word in the given text.
    Args:
        text (str): Input text
    Returns:
        dict: A dictionary where keys are words and values are their frequencies
    """
    pass


def Test1_Basic():
    text = "Algorithms, Algorithms, and more ALGORITHMS! Data is everywhere, DATA!"
    expected = {
        "algorithms": 3,
        "and": 1,
        "more": 1,
        "data": 2,
        "is": 1,
        "everywhere": 1,
    }
    res = word_frequency_counter(text)
    # Modify comparison, if necessary:
    assert res == expected


def Test2_LoremIpsum():
    text = '''
    Lorem ipsum dolor sit amet, lorem ridens pri cu, quas epicuri vivendum no mel. Vim te altera luptatum, no duo facete oblique petentium. Tota dolore tincidunt cum id, est at mutat simul, et per causae vocent. Modo feugait mea ex, dicat invidunt eam ea. An pri aperiam numquam luptatum, ei his option cotidieque persequeris.
    
    Te possim consetetur per, cu tritani sadipscing est. Ei rebum facer aliquip eum, mollis imperdiet dissentiunt per an. Cu usu legimus inermis, an his doming platonem. Cu per labitur prodesset mnesarchum, duo justo mazim ocurreret ex, ea nec vivendo efficiantur.
    
    Illum tincidunt ius et. Qui erat posidonium eu, mucius aliquip perpetua quo ad, mucius electram qui et. Dicta consectetuer id mel. At quo impedit probatus evertitur, per agam viderer cu, porro movet delicata quo te. Ne hinc feugait mei. Mei ne veri detraxit laboramus, ex mel clita theophrastus.
    
    Ad quem menandri suscipiantur cum, ne per libris nominati. Case copiosae atomorum an quo, vix corrumpit iracundia ex, sed partem reformidans ne. Id fabulas scaevola mei, salutandi ocurreret id qui. No qui soleat timeam, animal regione ei sed, no mei tale meliore. Ut eam diam salutandi deterruisset, no idque facilisi pro. Ad est aperiri disputando, vel noster possit moderatius ne, te eam rebum aliquid conclusionemque.
    
    Nihil verear vel ad, eos id viderer accusam. Et vis purto docendi, id usu omnes minimum. Ea duo decore maiorum. Sit debet efficiantur id, meliore delicatissimi vix et. Sea cu saepe honestatis neglegentur, has no noster utroque.
    '''
    frequencies = word_frequency_counter(text)

    # Modify access to the hashtable, if necessary:
    assert frequencies['lorem'] == 2
    assert frequencies['et'] == 5
    assert frequencies['cu'] == 6
    assert frequencies['id'] == 7


def Test3_KSE():
    text = '''
    KSE University, also known as the Kyiv School of Economics, is one of the leading institutions in Eastern Europe. Dedicated to providing world-class education, KSE focuses on economics, public policy, and business management. Founded with the mission of fostering development and academic excellence, kse has grown into a hub for students seeking global opportunities.

    At KSE, students benefit from rigorous academic training combined with hands-on experience. The university prides itself on its faculty, which includes internationally recognized scholars. Through innovative research and teaching, Kse equips students with tools needed to excel in a fast-changing world.
    
    One key feature of kse, is its strong focus on collaboration. Hosting workshops, events, and conferences, KSE attracts academics and policymakers worldwide. These initiatives enrich learning and provide kse-students with real-world insights.
    
    Moreover, kse's research centers address issues in policy, digital transformation, and sustainability. Graduates often achieve remarkable success, reinforcing KSE's reputation as a thought leader.
    
    Whether through its facilities, curriculum, or vibrant campus, kSe shapes education's future. For aspiring economists, KSE? is the destination.
    '''

    frequencies = word_frequency_counter(text)
    # Modify access to the hashtable, if necessary:
    assert frequencies['kse'] == 12
    assert frequencies['the'] == 5
    assert frequencies['and'] == 7
    assert frequencies['students'] == 4


if __name__ == "__main__":
    Test1_Basic()
    Test2_LoremIpsum()
    Test3_KSE()
