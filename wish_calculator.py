import datetime

def genshin():
    
    def pulls_from_glitter(pull, g):
        g = g + ((pull//90)*10) + (((pull-(pull//90))//10)*2)
        if g < 5:
            return pull
        return pulls_from_glitter(g//5, g%5)+pull

    count = int(input("How many banners to check for? "))
    primos = 0
    primos += int(input("Primos currently owned: "))
    pulls = int(input("Wishes currently owned: "))
    glitter = int(input("Masterless starglitter currently owned: "))
    crystals = int(input("Crystals currently owned: "))
    abyss = int(input("Estimated primos from abyss: ")) # 0.5 month
    welkin = 60 if str.lower(input("Welkin? [Y/N] : ")) == 'n' else 150
    print('----------------------------------------------------')
    trial = 40 # 21 days
    compensation = 300 + 600 # 42 days
    v2_0 = datetime.datetime(2021, 7, 21)
    curr_t = datetime.datetime.today()
    v = 2+(((curr_t - v2_0).days // 42)/10)
    snd_half = ((curr_t - v2_0).days // 21) % 2  # odd: 2nd half, even: 1st half
    rewards = {1:(5*160)+abyss, 4:20, 11:20, 16:abyss, 18:20}

    print("Currently at Version", v, "with primos:", primos, "fates:", pulls)
    print("Note: \n\t 1. Exclusive of day of calculation, inclusive of actual banner day;")
    print('\t 2. Starglitter wishes assume no overflowed characters, and one 5 star every 90 pull;')
    print('\t 3. Does not account for normal wishes')
    print('\t 4. Does not assume BP and event rewards')
    print('----------------------------------------------------\n')

    for i in range(count):
        old_t = curr_t - datetime.timedelta(days=1)
        if i == 0:
            day0 = 21 - ((curr_t - v2_0).days % 21)
            primos += day0*welkin
            curr_t += datetime.timedelta(days=day0)
        else:
            primos += 21*welkin
            curr_t += datetime.timedelta(days=21)
        if snd_half:
            primos += compensation
        v += (0.1*snd_half)
        snd_half = (snd_half + 1) % 2
        primos += trial
        for (k,val) in rewards.items():
            if (old_t.month < curr_t.month):
                if (curr_t.day >= k) or (k > old_t.day):
                    primos += val
            else:
                if (curr_t.day >= k) and (k > old_t.day):
                    primos += val
        crystals += 210
        
        pull_1 = (primos//160)+pulls
        pull_2 = pulls_from_glitter(pull_1, glitter)
        pull_3 = pulls_from_glitter(((primos+crystals)//160)+pulls, glitter)
        print("Version", round(v,1), (lambda x: "Second" if x else"First")(snd_half), "banner [", curr_t.date(), "]:")
        print("Total of", primos, "primos +", pulls, "pulls =", pull_1, "wishes")
        print("Wishes from starglitter shop =", pull_2)
        print("Wishes from using crystals + starglitter =", pull_3, "\n")
