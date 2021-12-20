import reviewer_query as r_query


if __name__ == "__main__":
    businesses = r_query.find_buz_at("lake pleasant and happy valley")        
    print(len(businesses))
    for bus in businesses:
        print(bus.name)