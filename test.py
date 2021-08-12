from testinlabel.TLA import TLA

ak = "ae1bdbc2d15e4fb4779558f75de21c95"
sk = "29de907568f60c9a452f24ef1e0a03b0"

tla = TLA(accessKey="ae1bdbc2d15e4fb4779558f75de21c95", secretKey=sk, debug=True)

tla.SetKey("210723e32ad")

tla.GetLabelData()
