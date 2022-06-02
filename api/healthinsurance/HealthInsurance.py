import pandas as pd
import numpy as np
import pickle


class HealthInsurance(object):
    def __init__( self ):

        self.annual_premium_scaler            = pickle.load ( open( '/Users/adriele/Documents/repos/pa004/features/annual_premium_scaler.pkl', 'rb') )
        self.age_scaler                       = pickle.load ( open( '/Users/adriele/Documents/repos/pa004/features/age_scaler.pkl', 'rb') )
        self.vintage_scaler                   = pickle.load ( open( '/Users/adriele/Documents/repos/pa004/features/vintage_scaler.pkl', 'rb') )
        self.target_encode_region_code_scaler = pickle.load ( open( '/Users/adriele/Documents/repos/pa004/features/target_encode_region_code_scaler.pkl', 'rb') )
        self.target_encode_gender_scaler      = pickle.load ( open( '/Users/adriele/Documents/repos/pa004/features/target_encode_gender_scaler.pkl', 'rb') )
        self.fe_policy_sales_channel_scaler   = pickle.load ( open( '/Users/adriele/Documents/repos/pa004/features/fe_policy_sales_channel_scaler.pkl', 'rb') )


    def data_cleaning( self, df1 ):

        # rename columns
        df1.columns = ['id', 'gender', 'age', 'region_code', 'policy_sales_channel',
                       'driving_license', 'vehicle_age', 'vehicle_damage',
                       'previously_insured', 'annual_premium', 'vintage', 'response']
        
       
        
        return df1

    def feature_engineering( self, df2 ):


        # Vehicle demage
        df2['vehicle_damage'] = df2['vehicle_damage'].apply( lambda x: 1 if x == 'yes' else 0)

        # Vehicle age
        df2['vehicle_age'] = df2['vehicle_age'].apply( lambda x: 'over_2_years' if x == '> 2 Years' else 'between_1_2_years' if x == '1-2 Year' else 'below_1_year')

        return df2

    # =========================================================================================

    def data_preparation( self, df5):

        # Annual Premium
        df5['annual_premium'] = self.annual_premium_scaler.transform( df5[[ 'annual_premium']].values)

        # age
        df5['age'] = self.age_scaler.transform(df5[['age']].values)

        # Vintage
        df5['vintage'] = self.vintage_scaler.transform( df5[['vintage']].values)

        # Region Code
        df5.loc[:, 'region_code'] = df5['region_code'].map( self.target_encode_region_code_scaler )

        # gender
        df5.loc[:, 'gender'] = df5['gender'].map( self.target_encode_gender_scaler )

        # vehicle_age
        df5 = pd.get_dummies( df5, prefix='vehicle_age', columns=['vehicle_age'] )

        # policy_sales_channel
        df5.loc[:, 'policy_sales_channel'] = df5['policy_sales_channel'].map(  self.fe_policy_sales_channel_scaler  )


        cols_selected = ['vintage','annual_premium', 'age', 'region_code','vehicle_damage',
                         'previously_insured', 'policy_sales_channel', 'gender']

        return df5[ cols_selected]


    def get_prediction( self, model, original_data, test_data):

        #prediction
        pred = model.predict_proba( test_data)

        # Join pred into original data
        original_data['score'] = pred[:, 1].tolist()

        return original_data.to_json( orient='records', date_format='iso' )






