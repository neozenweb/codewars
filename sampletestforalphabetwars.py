reinforces=["g964xxxxxxxx",
            "myjinxin2015",
            "steffenvogel",
            "smile67xxxxx",
            "giacomosorbi",
            "freywarxxxxx",
            "bkaesxxxxxxx",
            "vadimbxxxxxx",
            "zozofouchtra",
            "colbydauphxx" ]
airstrikes=["* *** ** ***",
            " ** * * * **",
            " * *** * ***",
            " **  * * ** ",
            "* ** *   ***",
            "***   ",
            "**",
            "*",
            "*" ]
           
test.assert_equals(alphabet_war(reinforces, airstrikes), 'codewarsxxxx','Top 50 massacre failure');
test.assert_equals(alphabet_war(["abcdefg","hijklmn"], ["   *   ", "*  *   "]),'hi___fg');               
test.assert_equals(alphabet_war(["aaaaa","bbbbb", "ccccc", "ddddd"],  ["*", " *", "   "]),'ccbaa');
