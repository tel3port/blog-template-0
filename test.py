x_list = ['accounting-scam.capterra-reviews.us',
          'android-scam.capterra-reviews.us',
          'auto-repair-scam.capterra-reviews.us',
          'bakeries.superpages-listings.us',
          'banking-scam.capterra-reviews.us',
          'banquet-rooms.superpages-listings.us',
          'bookkeeping-scam.capterra-reviews.us',
          'bowling-alley.superpages-listings.us',
          'cable-tv.superpages-listings.us',
          'car-rental-scam.capterra-reviews.us',
          'carpet-cleaning-scam.capterra-reviews.us',
          'catering-scam.capterra-reviews.us',
          'chinese-food.superpages-listings.us',
          'church-scam.capterra-reviews.us',
          'dentist-scam.capterra-reviews.us',
          'distance-learning-scam.capterra-reviews.us',
          'ecommerce.capterra-reviews.us',
          'email-scam.capterra-reviews.us',
          'fitness-scam.capterra-reviews.us',
          'gaming-scam.capterra-reviews.u',
          'job-scam.capterra-reviews.us',
          'liquor-stores.superpages-listings.us',
          'marine-scam.capterra-reviews.us',
          'martial-arts.superpages-listings.us',
          'painters.superpages-listings.us',
          'party-supplier.superpages-listings.us',
          'pediatric-dentist.superpages-listings.us',
          'pest-control.superpages-listings.us',
          'phone-scam.capterra-reviews.us',
          'psychic.superpages-listings.u',
          'scrap-metal-buyer.superpages-listings.us',
          'self-storage.superpages-listings.us',
          'sporting-goods.superpages-listings.us',
          'sprinkler-systems.superpages-listings.us',
          'tanning-salon.superpages-listings.us',
          'taxation-scam.capterra-reviews.us',
          'temporary-jobs.superpages-listings.us',
          'transmission-repair.superpages-listings.us',
          'weebly-scam.capterra-reviews.us',
          'superpages-listings.us',
          'capterra-reviews.us',
          'worst-restaurants.superpages-listings.us',
          ]

for x in x_list:
    if'superpages' in x:
    # print("ALLOWED_HOSTS = [")
    # print(f'"{"127.0.0.1"}",')
    # print(f'"{x}",')
        print(f'https://www.{x}')
    # print("]")
    # print()
