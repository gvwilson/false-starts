PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "sites" (
"site" TEXT,
  "lon" REAL,
  "lat" REAL
);
INSERT INTO sites VALUES('COT',-124.04519000000000517,48.821719999999997341);
INSERT INTO sites VALUES('YOU',-124.19700000000000184,48.872510000000000118);
INSERT INTO sites VALUES('HMB',-124.1755500000000012,48.81673000000000151);
INSERT INTO sites VALUES('GBY',-124.45930000000000603,48.920900000000004936);
CREATE TABLE IF NOT EXISTS "surveys" (
"label" INTEGER,
  "site" TEXT,
  "date" TEXT
);
INSERT INTO surveys VALUES(1748,'COT','2023-04-27');
INSERT INTO surveys VALUES(1749,'COT','2023-04-28');
INSERT INTO surveys VALUES(1755,'COT','2023-05-13');
INSERT INTO surveys VALUES(1781,'YOU','2023-05-01');
INSERT INTO surveys VALUES(1790,'HMB','2023-05-02');
INSERT INTO surveys VALUES(1803,'GBY','2023-05-08');
CREATE TABLE IF NOT EXISTS "samples" (
"label" INTEGER,
  "lon" REAL,
  "lat" REAL,
  "reading" REAL
);
INSERT INTO samples VALUES(1748,-124.04517999999999933,48.821710000000004825,106.89999999999999502);
INSERT INTO samples VALUES(1748,-124.04500000000000525,48.821599999999998331,81.699999999999999289);
INSERT INTO samples VALUES(1748,-124.04478000000001003,48.822000000000000952,57.400000000000002131);
INSERT INTO samples VALUES(1748,-124.04535000000000977,48.821419999999999816,73.499999999999996447);
INSERT INTO samples VALUES(1748,-124.04519000000000517,48.821589999999996933,89.100000000000001421);
INSERT INTO samples VALUES(1748,-124.04515999999998765,48.821710000000004825,91.699999999999999289);
INSERT INTO samples VALUES(1748,-124.04456999999999844,48.821039999999999992,12.0);
INSERT INTO samples VALUES(1748,-124.0444799999999903,48.82177000000000433,57.400000000000002131);
INSERT INTO samples VALUES(1748,-124.04549000000000269,48.821789999999998244,83.0);
INSERT INTO samples VALUES(1748,-124.04591000000000367,48.821880000000001942,38.700000000000001065);
INSERT INTO samples VALUES(1748,-124.04534000000000393,48.820860000000001477,3.7999999999999998223);
INSERT INTO samples VALUES(1748,-124.04524000000001215,48.821579999999995536,81.600000000000001421);
INSERT INTO samples VALUES(1748,-124.04528999999999694,48.821700000000003427,112.20000000000001083);
INSERT INTO samples VALUES(1748,-124.04451000000000782,48.821309999999993323,34.89999999999999769);
INSERT INTO samples VALUES(1748,-124.04486999999999596,48.822239999999998971,34.500000000000001776);
INSERT INTO samples VALUES(1748,-124.04456999999999844,48.820969999999999089,3.7000000000000001776);
INSERT INTO samples VALUES(1748,-124.04591000000000367,48.821560000000001622,40.700000000000002842);
INSERT INTO samples VALUES(1748,-124.04535000000000977,48.821269999999996613,48.0);
INSERT INTO samples VALUES(1748,-124.04587000000000251,48.821159999999999001,17.299999999999999822);
INSERT INTO samples VALUES(1748,-124.04459000000001012,48.821129999999994808,23.799999999999998934);
INSERT INTO samples VALUES(1748,-124.04398999999999286,48.821750000000001534,10.699999999999998401);
INSERT INTO samples VALUES(1748,-124.0450400000000064,48.821589999999996933,87.5);
INSERT INTO samples VALUES(1748,-124.04462999999998906,48.821719999999997341,61.500000000000003552);
INSERT INTO samples VALUES(1749,-124.04492999999998659,48.822099999999997166,46.500000000000003552);
INSERT INTO samples VALUES(1749,-124.04501000000001109,48.82175999999999405,95.199999999999995736);
INSERT INTO samples VALUES(1749,-124.0444799999999903,48.821589999999996933,50.80000000000000071);
INSERT INTO samples VALUES(1749,-124.04553000000000384,48.821789999999998244,72.5);
INSERT INTO samples VALUES(1749,-124.04527000000000747,48.821209999999997108,43.600000000000003197);
INSERT INTO samples VALUES(1749,-124.04448999999999614,48.821279999999998011,30.699999999999998401);
INSERT INTO samples VALUES(1749,-124.04508000000000755,48.821490000000000719,79.299999999999997157);
INSERT INTO samples VALUES(1749,-124.04515000000000402,48.821719999999997341,104.90000000000001545);
INSERT INTO samples VALUES(1749,-124.04520999999999464,48.821750000000001534,99.0);
INSERT INTO samples VALUES(1749,-124.0450400000000064,48.821589999999996933,60.299999999999993605);
INSERT INTO samples VALUES(1749,-124.04633000000000464,48.821599999999998331,13.800000000000001065);
INSERT INTO samples VALUES(1755,-124.04524000000001215,48.821729999999998739,90.700000000000002842);
INSERT INTO samples VALUES(1755,-124.04547999999999685,48.821810000000001039,76.400000000000005684);
INSERT INTO samples VALUES(1755,-124.04473000000000304,48.822069999999992973,53.200000000000002842);
INSERT INTO samples VALUES(1755,-124.04513999999999818,48.821700000000003427,84.400000000000012789);
INSERT INTO samples VALUES(1755,-124.0441600000000033,48.821159999999999001,1.6000000000000000888);
INSERT INTO samples VALUES(1755,-124.0447999999999995,48.822119999999999961,49.0);
INSERT INTO samples VALUES(1755,-124.04481000000000534,48.821320000000003602,51.0);
INSERT INTO samples VALUES(1755,-124.04535000000000977,48.821199999999995711,44.199999999999999289);
INSERT INTO samples VALUES(1755,-124.04516999999999349,48.821700000000003427,121.3999999999999968);
INSERT INTO samples VALUES(1755,-124.04431000000000206,48.821279999999998011,18.399999999999998578);
INSERT INTO samples VALUES(1755,-124.04417999999999278,48.821440000000002612,16.899999999999999467);
INSERT INTO samples VALUES(1755,-124.04513999999999818,48.821810000000001039,85.80000000000000071);
INSERT INTO samples VALUES(1755,-124.0447999999999995,48.82209000000000465,45.200000000000004618);
INSERT INTO samples VALUES(1755,-124.04418999999999861,48.821840000000005233,21.800000000000001598);
INSERT INTO samples VALUES(1755,-124.0438399999999941,48.82177000000000433,0.7);
INSERT INTO samples VALUES(1803,-124.45981000000001515,48.921630000000000393,26.699999999999999289);
INSERT INTO samples VALUES(1803,-124.4593199999999955,48.920909999999997452,70.90000000000000746);
INSERT INTO samples VALUES(1803,-124.46036000000000321,48.920979999999998355,38.100000000000001421);
INSERT INTO samples VALUES(1803,-124.45743000000000222,48.921010000000002548,1.7);
INSERT INTO samples VALUES(1803,-124.46048000000000666,48.920589999999997132,33.0);
INSERT INTO samples VALUES(1803,-124.46060999999999374,48.921660000000004586,7.9000000000000003552);
INSERT INTO samples VALUES(1803,-124.46004000000001621,48.920690000000002228,50.099999999999997868);
INSERT INTO samples VALUES(1803,-124.45828000000001001,48.920659999999998035,32.600000000000002309);
INSERT INTO samples VALUES(1790,-124.17565999999999881,48.817099999999999937,70.599999999999996092);
INSERT INTO samples VALUES(1790,-124.17644999999999377,48.816910000000000025,40.600000000000004973);
INSERT INTO samples VALUES(1790,-124.17534000000001181,48.817649999999996879,4.5);
INSERT INTO samples VALUES(1790,-124.17544999999998722,48.817120000000002733,48.700000000000001065);
INSERT INTO samples VALUES(1790,-124.17541000000000828,48.81673000000000151,111.49999999999999911);
INSERT INTO samples VALUES(1790,-124.17556000000000704,48.816709999999998714,117.19999999999999307);
INSERT INTO samples VALUES(1790,-124.1760299999999928,48.816800000000002413,46.100000000000003197);
INSERT INTO samples VALUES(1790,-124.1751500000000119,48.816630000000005296,62.599999999999997868);
INSERT INTO samples VALUES(1790,-124.17610000000001146,48.816569999999996909,77.0);
INSERT INTO samples VALUES(1790,-124.17633999999999616,48.816940000000004218,47.799999999999993605);
INSERT INTO samples VALUES(1790,-124.17574000000000111,48.817409999999998859,28.700000000000001065);
INSERT INTO samples VALUES(1790,-124.17678999999999245,48.816639999999997812,15.80000000000000071);
INSERT INTO samples VALUES(1790,-124.17523999999999784,48.816399999999999792,48.600000000000003197);
INSERT INTO samples VALUES(1790,-124.17641000000001483,48.816269999999999384,20.400000000000000355);
INSERT INTO samples VALUES(1790,-124.17578000000000226,48.81673000000000151,84.800000000000004263);
INSERT INTO samples VALUES(1790,-124.17588999999999987,48.816509999999997404,56.299999999999998934);
INSERT INTO samples VALUES(1790,-124.1759499999999905,48.816360000000003083,52.5);
INSERT INTO samples VALUES(1790,-124.17468000000000394,48.817219999999998947,21.100000000000003197);
INSERT INTO samples VALUES(1790,-124.1761099999999951,48.815919999999994871,12.099999999999999644);
INSERT INTO samples VALUES(1781,-124.196989999999996,48.872499999999998721,96.600000000000001421);
INSERT INTO samples VALUES(1781,-124.1970699999999983,48.872809999999997643,70.0);
INSERT INTO samples VALUES(1781,-124.19808000000001069,48.872879999999998545,41.699999999999999289);
INSERT INTO samples VALUES(1781,-124.19678000000000661,48.872710000000001429,87.599999999999997868);
INSERT INTO samples VALUES(1781,-124.19724999999999237,48.872540000000004312,83.799999999999990052);
INSERT INTO samples VALUES(1781,-124.19829000000000007,48.871549999999999158,5.4000000000000003552);
INSERT INTO samples VALUES(1781,-124.19696000000000069,48.872499999999998721,72.799999999999993605);
INSERT INTO samples VALUES(1781,-124.19736999999999582,48.872309999999998808,74.900000000000002131);
INSERT INTO samples VALUES(1781,-124.19668999999999847,48.872680000000006117,43.0);
INSERT INTO samples VALUES(1781,-124.19704000000000299,48.872569999999999623,94.199999999999999289);
INSERT INTO samples VALUES(1781,-124.19734000000000051,48.87357999999999869,15.900000000000000355);
INSERT INTO samples VALUES(1781,-124.19670000000000431,48.873780000000000001,4.5);
COMMIT;
