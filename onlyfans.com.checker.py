from enum import verify
from math import fabs
import execjs
import requests
import json
import re
import base64
import time
import hashlib

js_code = '''
 function t(W, n) {
                    return o(n - 967, W)
                }
 function o(W, n) {
                return k(W - -779, n)
            }
  function C() {
            var W = ["W4NcKKVdTW", "W4nWWQJcNMu", "W5xdUCoOsmkpW6C", "iNddQ8ochYNcQJ3dR8k0", "i0fAoSos", "WRzko00D", "vttcPs85W4NcGuW", "WRv0WRVdLSoDhSot", "WP/dP8oSuCohbCkCrCkpWQC", "lxOTpwTCeG", "WPipW5xdQmkLcG", "CSkYCCkLBCo8", "yLJdJSkWWOpdJWJcQ8kQimoEEmk+W47cRrxcU2jEomofk39EW7DiWQhcGSkUWOaZWPa", "ghmGFCou", "v8kBgIzp", "hgOWW4JdTq", "WO0yWQzzWOXQjuHhWR3dV1CJ", "W6dcH8kFlmoX", "lmoCnNldJq", "WRddVCoeCCkiWO0jWQpdGbPLya", "uSkMhdD8WRvEFrJcVG", "W5JcTwaMW6O", "W4rIlCobWPe", "W4PEWO/cT8oIuCkbs1hcINelW5O", "ixCSx8o0", "DGmrorBdVaLKb0C", "WOSTW7NdGIi", "eeNdHsmP", "lx3dPmoxkc4", "hSk9x8oMkW", "B8kwACkbpa", "W5rbfmozWQfvWOJcLGCN", "W4jBgq", "W6f7WRpdGZfqWRtdSmokmG", "WRT4bL0K", "zr0pECkpWPvGW4KorNRdJG", "AtTZpqK", "DSkfuSkBwW", "AmotWQv+lG", "h2a8W5pdKa", "ySkNW7hcTSklW5xcTCocmCkbWR1Bjq", "teqTehO", "tSk7WPSrFCoZ", "ix8OW7JdIq", "FCk8WPuYW4u", "p8ozWOldImo2", "W4PNW4OlW4W", "oCoIW5/cMCoa", "W4HgW5C7W5i", "W5/dMmoivSkq", "Df3cLSo3WOxcLIxcMCkOba", "mSkOW7qWW5y", "W7VdTCkjW5dcHH5BWP8yWQdcP8kwvq", "WQ3dKZtdUmo4", "fCo0ugRdQdK", "W5PeW7mtW7W2D0TnWQ0", "WPVdKIzFBa", "DmoWkMpdG8ouW43cUdFcUchcKtO", "WQjHmwyMWOD9W5e1W5G", "WRNdKZrbwKamWOFdGGa", "WOtcNSkQCCkmFq", "WPtdNCoaESog", "WQFdSXBdImoh", "dMCyu8oHma", "FCk/FSkWwSo7WPH/brC", "FY9leZXd", "DCkUW5m2BCoqD8oJcCknd8ksA8og", "WOZdSSoTW5qM", "l8oFjguM", "WRrEa0Cr", "iNGqhGzOeCkKCG", "WQVcNCknuCk7", "meldMSoslq", "W7dcTmkAhSk4", "WOVdJmoMESo8", "WOKLW6VdRCkc", "WO/dHmovsCo3", "ev3dVCoNma", "W7CmWQnzW5m", "W69lWPVdPZ8", "ANSYiuLXjSoO", "WQ1SpNmrWOa", "WPNdNmkLW4S7dtldQZOC", "W454WRXRWPOn", "WP3dMSoiW70", "WQhcMmkYxmkU", "CCo4WQDToG", "DLFcHa", "WPKpW4/dU8k0emoea3VcM1CTWQbOW57dNSoDoI3dQColvSkM", "WRRdM3K2pCkjWPOmo8kj", "i1GmW47dIG", "W74LWQJcJG", "agRdVdSzWPpcGe/dOCos", "W5JcGSktWQ1KWOb/zHldStFdLq", "W41yi8oIWQm", "W6mRWPjjW4nAA8oMaIy", "W69DWOddMrW", "iSkTtYFcSa", "W4RcJSkVgCkFW7CUWPSrCW", "jSkMDdG", "WPDTi2qp", "oCkWDmoJea", "i0euW7VdRq", "WOJdLsZdLCoAW5O", "DCkHWOO7W6Se", "dmoHW4hcSCod", "W6KKWQtcMCowW7f7WQxcNXS", "WPenW67dVSkL", "mmofWQFdPSoi", "W652WRZdLGzx", "W63cMCkXhCo+", "jeCoj8oW", "ddFdJ8kxW5FcUNDUW6/dRG", "W6yPWQVcJmoHW7y", "amo8thqiW6GiEW7cJ3FcKNa", "ACoOW5ewW7ZdVSkOsW", "W5lcO2JdO1e", "W6NcRSksi8oiW5W", "W4K6WORcK8oL", "W5hcISksWQ1MWOSlzttdNXFdO8oH", "nmk5W54HW4VdHG", "iSoShLBdGXZdQ2NdPmk4", "W6CcWPFcG8o7", "W5RdTmoNxCk4W6dcLSkpW4Lg", "amo0WRpdTCos", "imkSCZhcG8kf", "W7f3WPtdImoM", "W6b+W4yuW5S", "W5ZcSCkDomkO", "mSoAoM8q", "W5KPWQlcHSog", "A8oVWR5zja", "jGFdGSoVWOJcUHlcMSk+", "k8oOb1SqaG", "jf8rgXBdGZ1V", "Cmk2ACkRFSo1WOH1nK1ZWRRdJ8kKiY7dLIrJ", "W6L1t8kHW4hdRce3zmo3", "WP0cW5RdVCksdCotsfVcMG", "Emo+lgxdHmoFW47cHdZcHG/cRsK", "W4LRyCkRW7i", "pmo/WQNdQW", "kuC8W5pdOmkDp8o3qCkf", "W5fwWOPMWP0", "WPpdVXldKmo9", "W5b/WRVdOcS", "ASosWPLOhCkt", "W6WMWP1CW7rD", "l0qWm8o4", "i8ohWPpdLSom", "B3mqj0i", "pSkGzmo/cCohW4NdLxZcJq", "CcjebGTejSkNzmkO", "WRCjW43dHCkh", "jmoLce4NbCkHWRVcTM8", "jGtdHSk9W7ldGhJdJmkAa8o1w8k0W5m", "kmo6WOXPlCkb", "jgzijSoZ", "ECo/jwpdG8ouWOBcMcRcOt3cQG"];
            return (C = function() {
                return W
            }
            )()
        }
    function k(W, n) {
            const o = C();
            return k = function(n, t) {
                let c = o[n -= 289];
                if (void 0 === k.KKHIlG) {
                    var r = function(W) {
                        const n = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+/=";
                        let o = ""
                          , t = "";
                        for (let c = 0, r, u, i = 0; u = W.charAt(i++); ~u && (r = c % 4 ? 64 * r + u : u,
                        c++ % 4) ? o += String.fromCharCode(255 & r >> (-2 * c & 6)) : 0)
                            u = n.indexOf(u);
                        for (let c = 0, r = o.length; c < r; c++)
                            t += "%" + ("00" + o.charCodeAt(c).toString(16)).slice(-2);
                        return decodeURIComponent(t)
                    };
                    const n = function(W, n) {
                        let o = [], t = 0, c, u = "", i;
                        for (W = r(W),
                        i = 0; i < 256; i++)
                            o[i] = i;
                        for (i = 0; i < 256; i++)
                            t = (t + o[i] + n.charCodeAt(i % n.length)) % 256,
                            c = o[i],
                            o[i] = o[t],
                            o[t] = c;
                        i = 0,
                        t = 0;
                        for (let r = 0; r < W.length; r++)
                            i = (i + 1) % 256,
                            t = (t + o[i]) % 256,
                            c = o[i],
                            o[i] = o[t],
                            o[t] = c,
                            u += String.fromCharCode(W.charCodeAt(r) ^ o[(o[i] + o[t]) % 256]);
                        return u
                    };
                    k.womakW = n,
                    W = arguments,
                    k.KKHIlG = !0
                }
                const u = undefined
                  , i = n + o[0]
                  , e = W[i];
                return e ? c = e : (void 0 === k.cdnRwA && (k.cdnRwA = !0),
                c = k.womakW(c, t),
                W[i] = c),
                c
            }
            ,
            k(W, n)
        }
			
			  function o(W, n) {
                return k(W - -779, n)
            }
			
			!function(W, n) {
				function o(W, n) {
					return k(n - -725, W)
				}
				const t = W();
				for (; ; )
					try {
						const W = undefined;
						if (parseInt(o("nt8!", -424)) / 1 + -parseInt(o("s(pC", -329)) / 2 + -parseInt(o("DNZ*", -436)) / 3 * (parseInt(o("cAmi", -420)) / 4) + -parseInt(o("czii", -311)) / 5 * (-parseInt(o("^rJh", -350)) / 6) + parseInt(o("cKvk", -328)) / 7 * (parseInt(o("Yx5h", -305)) / 8) + -parseInt(o("Yx5h", -386)) / 9 + parseInt(o("O58S", -377)) / 10 === n)
							break;
						t.push(t.shift())
					} catch (c) {
						t.push(t.shift())
                }
        }(C, 635831);
   function getsalt(){
			return o(-485, "czii");
		}
function getsign(sha1_str){
	var n = {
                mNRhn: function(W, n) {
                    return W + n
                },
                Aislu: function(W, n) {
                    return W + n
                },
                SegmS: function(W, n) {
                    return W + n
                },
                IcvJV: function(W, n) {
                    return W + n
                },
                cgmXi: function(W, n) {
                    return W + n
                },
                Vdspj: function(W, n) {
                    return W + n
                },
                dxqnZ: function(W, n) {
                    return W + n
                },
                jtDvi: function(W, n) {
                    return W + n
                },
                RPLEA: function(W, n) {
                    return W + n
                },
                eAHLt: function(W, n) {
                    return W + n
                },
                sKXjs: function(W, n) {
                    return W + n
                },
                ndRqG: function(W, n) {
                    return W + n
                },
                CuZka: function(W, n) {
                    return W + n
                },
                zkbdu: function(W, n) {
                    return W + n
                },
                wCkYx: function(W, n) {
                    return W + n
                },
                qjEZm: function(W, n) {
                    return W + n
                },
                PEwWl: function(W, n) {
                    return W + n
                },
                pJqjJ: function(W, n) {
                    return W + n
                },
                zqVIA: function(W, n) {
                    return W - n
                },
                mXIVM: function(W, n) {
                    return W % n
                },
                wmcvk: function(W, n) {
                    return W - n
                },
                wOPbS: function(W, n) {
                    return W % n
                },
                iwQoi: function(W, n) {
                    return W - n
                },
                uWSSt: function(W, n) {
                    return W % n
                },
                RliQY: function(W, n) {
                    return W % n
                },
                hRMYB: function(W, n) {
                    return W - n
                },
                eLchM: function(W, n) {
                    return W + n
                },
                UOars: function(W, n) {
                    return W % n
                },
                qgqry: function(W, n) {
                    return W % n
                },
                CvOxp: function(W, n) {
                    return W % n
                },
                fUgcp: function(W, n) {
                    return W - n
                },
                fDNyk: function(W, n) {
                    return W % n
                },
                CCTzi: function(W, n) {
                    return W + n
                },
                CFawj: function(W, n) {
                    return W % n
                },
                YRTud: function(W, n) {
                    return W % n
                },
                VEmiV: function(W, n) {
                    return W % n
                },
                inIZN: function(W, n) {
                    return W - n
                },
                kPuYj: function(W, n) {
                    return W + n
                },
                qZPbq: function(W, n) {
                    return W % n
                },
                CfIGC: function(W, n) {
                    return W + n
                },
                YoWEQ: function(W, n) {
                    return W % n
                },
                ogUqt: function(W, n, o, t) {
                    return W(n, o, t)
                },
                iIBMN: function(W, n) {
                    return W(n)
                },
                hXDzL: o(-485, "czii")
            }
var W=sha1_str;
	return Math[t("czii", 557)](n[t("VpBY", 592)](n[t("DIi@", 526)](n[t("*jqi", 566)](n[t("VpBY", 600)](n[t("#UOP", 523)](n[t("sCaF", 575)](n[t("sCaF", 517)](n[t("SFeJ", 570)](n[t("cAmi", 622)](n[t("!E8O", 571)](n[t("cKvk", 521)](n[t("P@*V", 511)](n[t("^rJh", 537)](n[t("IuYQ", 546)](n[t("Yx5h", 567)](n[t("!E8O", 499)](n[t("N3hK", 496)](n[t("IuYQ", 544)](n[t("ig9^", 518)](n[t("fd3p", 494)](n[t("SFeJ", 633)](n[t("ig9^", 516)](n[t("eN)i", 547)](n[t("QgU3", 492)](n[t("*&XS", 626)](n[t("J0gn", 506)](W[n[t("*jqi", 549)](27088, W[t("]ebt", 574)])][t("eN)i", 631)](0), 81) + n[t("DNZ*", 596)](W[n[t("5zQm", 556)](28617, W[t("HTlt", 603)])][t("G%t@", 559)](0), 78), n[t("6Fq4", 560)](W[26754 % W[t("O58S", 625)]][t("nBmi", 606)](0), 89)), W[n[t("sK$m", 618)](27770, W[t("593D", 524)])][t("5)#2", 582)](0) + 148), W[n[t("(BeO", 581)](28727, W[t("Yx5h", 595)])][t("!E8O", 620)](0) - 80), n[t("IuYQ", 531)](W[27223 % W[t("cAmi", 480)]][t("8WJs", 568)](0), 110)), n[t("yhax", 497)](W[n[t("cAmi", 545)](27455, W[t("V)VA", 530)])][t("yhax", 562)](0), 153)), n[t("nt8!", 487)](W[n[t("NH9I", 548)](26593, W[t("fd3p", 533)])][t("yhax", 562)](0), 75)), n[t("fd3p", 483)](W[n[t("SFeJ", 539)](27528, W[t("HTlt", 603)])][t("[P$B", 552)](0), 81)) + n[t("5zQm", 508)](W[n[t("6Fq4", 509)](27023, W[t("hTg(", 630)])][t("nBmi", 606)](0), 67), n[t("wxyO", 612)](W[27648 % W[t("nt8!", 587)]][t("s(pC", 490)](0), 120)), n[t("SFeJ", 504)](W[n[t("P@*V", 619)](26971, W[t("eN)i", 498)])][t("[P$B", 552)](0), 94)), W[n[t("*jqi", 614)](26433, W[t("5zQm", 615)])][t("8WJs", 568)](0) - 52), n[t("nt8!", 580)](W[n[t("VpBY", 588)](28005, W[t("ths]", 481)])][t("NH9I", 565)](0), 110)), W[n[t("qbCE", 488)](27333, W[t("Yx5h", 595)])][t("czii", 520)](0) + 115), n[t("sK$m", 578)](W[n[t("XR!t", 500)](28953, W[t("O58S", 625)])][t("6Fq4", 611)](0), 142)), n[t("#UOP", 532)](W[27136 % W[t("593D", 524)]][t("SFeJ", 528)](0), 48)), n[t("ths]", 507)](W[n[t("m8$W", 491)](28494, W[t("#UOP", 573)])][t("0X%N", 495)](0), 87)), W[n[t("hTg(", 519)](28548, W[t("O58S", 625)])][t("*jqi", 503)](0) + 58) + n[t("*&XS", 632)](W[n[t("#UOP", 613)](28836, W[t("wxyO", 553)])][t("IuYQ", 478)](0), 113), n[t("HTlt", 538)](W[n[t("ig9^", 597)](27900, W[t("5zQm", 615)])][t("DIi@", 529)](0), 105)), W[n[t("6Fq4", 485)](28267, W[t("NH9I", 616)])][t("ig9^", 525)](0) + 91) + n[t("QgU3", 564)](W[n[t("8WJs", 598)](27823, W[t("ths]", 481)])][t("VpBY", 576)](0), 68), n[t("sK$m", 594)](W[n[t("HTlt", 599)](28187, W[t("J0gn", 535)])][t("cAmi", 607)](0), 129)), n[t("V)VA", 555)](W[n[t("8WJs", 543)](28085, W[t("HTlt", 603)])][t("J0gn", 621)](0), 101)), n[t("6Fq4", 572)](W[28334 % W[t("hTg(", 630)]][t("0X%N", 495)](0), 81)) + (W[28421 % W[t("eN)i", 498)]][t("HTlt", 623)](0) - 92), n[t("6Fq4", 513)](W[n[t("eN)i", 542)](26519, W[t("VpBY", 583)])][t("qbCE", 591)](0), 109)), n[t("V)VA", 541)](W[n[t("nBmi", 609)](26820, W[t("Eh5F", 512)])][t("!E8O", 620)](0), 70)) + n[t("]ebt", 514)](W[n[t("5zQm", 601)](26667, W[t("SFeJ", 551)])][t("hTg(", 593)](0), 85), n[t("s(pC", 484)](W[28670 % W[t("cKvk", 590)]][t("QgU3", 501)](0), 83)), W[n[t("(BeO", 617)](26904, W[t("*jqi", 579)])][t("ths]", 534)](0) + 108))[t("P@*V", 550)](16)
}
'''
# Configuration
CLEARCAPTCHA_API_KEY = 'test'
CAPTCHA_ENDPOINT = "http://api.clearcaptcha.com/captcha/recaptcha_enterprise_v2v3"
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0"
email="afdasfdsa@gmail.com"
password="123456";

headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'Sec-Ch-Ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Model': '""',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': USER_AGENT,
}

session = requests.Session()
response = requests.get("https://onlyfans.com/",verify=False)

post_data =  {
    "token": CLEARCAPTCHA_API_KEY,
    "sitekey": "6LcvNcwdAAAAAMWAuNRXH74u3QePsEzTm6GEjx0J",
    "referer":"https://www.onlyfans.com",
    "recaptcha_anchor_size":"invisible",
    "page_title":"OnlyFans",
    "action":"login",
}
response = requests.post(CAPTCHA_ENDPOINT, data=post_data,verify=False)
response_data = response.json()
recaptcha_token_invisible=response_data.get("data", {}).get("recaptcha_token", "")
print(f'reCaptcha Token: {recaptcha_token_invisible}')

encodedPassword=base64.b64encode(password.encode('utf-8')).decode('utf-8')
post_data = {
    "email": email,
    "encodedPassword":encodedPassword,
    "e-recaptcha-response":recaptcha_token_invisible,
    # "ec-recaptcha-response":recaptcha_token_normal
}
ctx = execjs.compile(js_code)
sign_salt=ctx.call('getsalt')
print(f'Sign Salt: {sign_salt}')

unix_time= str(int(time.time() * 1000))
sign_data=(
    sign_salt,
     unix_time,
    "/api2/v2/users/login",
    "0"
)
sign_str='\n'.join(sign_data)
sha1_hash = hashlib.sha1()

sha1_hash.update(sign_str.encode('utf-8'))
sign_str = sha1_hash.hexdigest()


checksum = ctx.call('getsign',sign_str)
sign_str=f"26382:{sign_str}:{checksum}:668fc5ef"

print(f'Sign: {sign_str}')
headers["Content-Type"]="application/json"
headers["app-token"]="33d57ade8c02dbc5a333db99ff9ae26a"
headers["sign"]=sign_str
headers["time"]=unix_time
headers["x-bc"]="b32cf0d237fbadba243c3a9084798a610ffacdf0"
headers["x-hash"]="JSQciRbfbujHQ2fjzrEk5jAQsU7Cit6uvm7ubw=="
headers["x-of-rev"]="202407111145-b8ced9ebec"

post_data=json.dumps(post_data)
print(post_data)
response = requests.post("https://onlyfans.com/api2/v2/users/login", headers=headers, data=post_data,verify=False)
print(f'Login response: {response.text}')
responsejson=response.json()
if responsejson["error"]["code"] == 102 :
    post_data =  {
        "token": CLEARCAPTCHA_API_KEY,
        "sitekey": "6LddGoYgAAAAAHD275rVBjuOYXiofr1u4pFS5lHn",
        "referer":"https://www.onlyfans.com",
        "recaptcha_anchor_size":"normal",
        "page_title":"OnlyFans",
        "sa":"login"
    }
    response = requests.post(CAPTCHA_ENDPOINT, data=post_data,verify=False)
    response_data = response.json()
    recaptcha_token_normal=response_data.get("data", {}).get("recaptcha_token", "")
    print(f'reCaptcha Token: {recaptcha_token_normal}')
    
    post_data = {
        "email": email,
        "encodedPassword":encodedPassword,
        "e-recaptcha-response":recaptcha_token_invisible,
        "ec-recaptcha-response":recaptcha_token_normal
    }
    post_data=json.dumps(post_data)
    response = requests.post("https://onlyfans.com/api2/v2/users/login", headers=headers, data=post_data,verify=False)
    print(f'Login response: {response.text}')