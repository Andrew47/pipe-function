def pipe(args = None):
    def pipe(fcns):
        if not hasattr(fcns, '__iter__'):
            return fcns(args)

        for fcn in enumerate(fcns):
            if fcn[0] == 0:
                fcn1 = fcn[1](args) if args is not None else fcn[1]()
            else:
                fcn1 = fcn[1](fcn1)
        return fcn1
    return pipe
