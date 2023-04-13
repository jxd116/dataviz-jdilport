Sub stock_analysis()
    
    'Loop through all worksheets
    For Each ws In Worksheets
    
        'Define variables
        Dim ticker As String
        Dim opening_price As Double
        Dim closing_price As Double
        Dim yearly_change As Double
        Dim percent_change As Double
        Dim total_volume As Double
        Dim last_row As Long
        Dim i As Long
        Dim j As Long
        Dim k As Long
        
        'Set headers for output columns
        ws.Cells(1, 9).Value = "Ticker"
        ws.Cells(1, 10).Value = "Yearly Change"
        ws.Cells(1, 11).Value = "Percent Change"
        ws.Cells(1, 12).Value = "Total Stock Volume"
        
        'Find last row
        last_row = ws.Cells(Rows.Count, 1).End(xlUp).Row
        
        'Loop through all rows in the sheet
        j = 2
        For i = 2 To last_row
            
            'Check if current ticker symbol is the same as the previous one
            If ws.Cells(i, 1).Value <> ws.Cells(i - 1, 1).Value Then
                
                'Set opening price and reset total volume for new ticker symbol
                opening_price = ws.Cells(i, 3).Value
                total_volume = 0
                
            End If
            
            'Add to total volume
            total_volume = total_volume + ws.Cells(i, 7).Value
            
            'Check if current row is the last row for the current ticker symbol
            If ws.Cells(i, 1).Value <> ws.Cells(i + 1, 1).Value Then
                
                'Set closing price
                closing_price = ws.Cells(i, 6).Value
                
                'Calculate yearly and percent change
                yearly_change = closing_price - opening_price
                If opening_price <> 0 Then
                    percent_change = yearly_change / opening_price
                Else
                    percent_change = 0
                End If
                
                'Output results
                ws.Cells(j, 9).Value = ws.Cells(i, 1).Value
                ws.Cells(j, 10).Value = yearly_change
                ws.Cells(j, 11).Value = percent_change
                ws.Cells(j, 12).Value = total_volume
                
                'Format output cells
                If yearly_change >= 0 Then
                    ws.Cells(j, 10).Interior.ColorIndex = 4 'Green
                Else
                    ws.Cells(j, 10).Interior.ColorIndex = 3 'Red
                End If
                ws.Cells(j, 11).NumberFormat = "0.00%"
                
                'Increment row counter
                j = j + 1
                
            End If
            
        Next i
        
        'Find last row in output range
        last_row = ws.Cells(Rows.Count, 9).End(xlUp).Row
        
      'Find greatest % increase, % decrease, and total volume
        Dim max_increase As Double
        Dim max_decrease As Double
        Dim max_volume As Double
        Dim max_increase_ticker As String
        Dim max_decrease_ticker As String
        Dim max_volume_ticker As String
        
        max_increase = WorksheetFunction.Max(ws.Range("K2:K" & last_row))
        max_decrease = WorksheetFunction.Min(ws.Range("K2:K" & last_row))
        max_volume = WorksheetFunction.Max(ws.Range("L2:L" & last_row))
        
        'Find ticker
        For k = 2 To last_row
            
            'Check for greatest % increase
            If ws.Cells(k, 11).Value = max_increase Then
                max_increase_ticker = ws.Cells(k, 9).Value
            End If
            
            'Check for greatest % decrease
            If ws.Cells(k, 11).Value = max_decrease Then
                max_decrease_ticker = ws.Cells(k, 9).Value
            End If
            
            'Check for greatest total volume
            If ws.Cells(k, 12).Value = max_volume Then
                max_volume_ticker = ws.Cells(k, 9).Value
            End If
            
        Next k
        
        'Output results
        ws.Cells(2, 15).Value = "Greatest % Increase"
        ws.Cells(3, 15).Value = "Greatest % Decrease"
        ws.Cells(4, 15).Value = "Greatest Total Volume"
        ws.Cells(1, 16).Value = "Ticker"
        ws.Cells(1, 17).Value = "Value"
        ws.Cells(2, 16).Value = max_increase_ticker
        ws.Cells(3, 16).Value = max_decrease_ticker
        ws.Cells(4, 16).Value = max_volume_ticker
        ws.Cells(2, 17).Value = Format(max_increase, "0.00%")
        ws.Cells(3, 17).Value = Format(max_decrease, "0.00%")
        ws.Cells(4, 17).Value = max_volume
        
        
    Next ws
    
End Sub
